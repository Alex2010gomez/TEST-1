document.addEventListener("DOMContentLoaded", () => {
  const contenedor = document.getElementById("contenedor");
  const formulario = document.getElementById("submit"); // O el form principal
  const busquedaInput = document.getElementById("busqueda");
  const filtroEstado = document.getElementById("filtroEstado");
  const contadoresContainer = document.getElementById("contadores");
  const btnTema = document.getElementById("toggleTema");

  let computadoras = [];
  let idEditando = null; // Guardará el id_equipo real de la base de datos

  // Cargar datos iniciales desde la API
  obtenerEquipos();

  // Escuchar filtros en tiempo real
  if (busquedaInput) busquedaInput.addEventListener("input", filtrarYBuscar);
  if (filtroEstado) filtroEstado.addEventListener("change", filtrarYBuscar);

  // Evento Guardar / Editar (Formulario)
  const formElement = document.querySelector("form") || formulario;
  if (formElement) {
    formElement.addEventListener('submit', async function (e) {
      e.preventDefault();

      const objetoCompu = {
        tipo_equipo: document.getElementById("TC").value,
        nombre_dueno: document.getElementById("dueno").value,
        marca_compu: document.getElementById("marca").value,
        procesador: document.getElementById("procesador").value,
        generacion: document.getElementById("gen").value,
        ram_cantidada: Number(document.getElementById("cram").value) || 0,
        tipo: document.getElementById("TRAM").value,
        almacenamiento_cantidad: Number(document.getElementById("Cdisco").value) || 0,
        almacenamiento_tipo: document.getElementById("tipodisco").value,
        grafica_modelo: document.getElementById("MGPU").value,
        grafica_tipo: document.getElementById("TGPU").value,
        tamanio_monitor: Number(document.getElementById("pantalla").value) || 0,
        estado: document.getElementById("estado").value
      };

      try {
        if (idEditando !== null) {
          // Petición PUT para actualizar
          const respuesta = await fetch(`/equipos/${idEditando}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(objetoCompu)
          });
          if (!respuesta.ok) throw new Error("Error al actualizar");
          idEditando = null;
        } else {
          // Petición POST para crear
          const respuesta = await fetch("/equipos", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(objetoCompu)
          });
          if (!respuesta.ok) throw new Error("Error al crear");
        }

        formElement.reset();
        await obtenerEquipos();
      } catch (error) {
        console.error("Error al guardar:", error);
        alert("No se pudo guardar el equipo en la base de datos.");
      }
    });
  }

  // Función para obtener equipos del servidor
  async function obtenerEquipos() {
    try {
      const respuesta = await fetch("/equipos");
      if (!respuesta.ok) throw new Error("Error al obtener equipos");
      computadoras = await respuesta.json();
      renderizarcomputadoras(computadoras);
    } catch (error) {
      console.error("Error:", error);
    }
  }

  function renderizarcomputadoras(listaAFiltrar = computadoras) {
    contenedor.innerHTML = "";
    listaAFiltrar.forEach((compu) => {
      const tarjetacompu = document.createElement('div');
      tarjetacompu.classList.add('tarjeta-compu');
      tarjetacompu.innerHTML = `
        <h3>${compu.marca_compu}</h3>
        <p>ID : ${compu.id_equipo}</p>
        <p>Estado: <strong>${compu.estado || 'Operativo'}</strong></p>
        <p>Tipo de computadora : ${compu.tipo_equipo}</p>
        <p>Dueño: ${compu.nombre_dueno}</p>
        <p>Marca del Procesador : ${compu.procesador} </p>
        <p>Procesador : ${compu.generacion}</p>
        <p>RAM: ${compu.ram_cantidada}GB ${compu.tipo}</p>
        <p>Capacidad: ${compu.almacenamiento_cantidad}GB ${compu.almacenamiento_tipo}</p>
        <p>GPU: ${compu.grafica_modelo} ${compu.grafica_tipo}</p>
        <p>Pantalla de ${compu.tamanio_monitor} pulgadas</p>
      `;

      const eliminar = document.createElement('button');
      eliminar.textContent = '❌';
      eliminar.addEventListener('click', async () => {
        if (confirm("¿Estás seguro de eliminar este equipo?")) {
          try {
            const resp = await fetch(`/equipos/${compu.id_equipo}`, { method: "DELETE" });
            if (!resp.ok) throw new Error("No se pudo eliminar");
            await obtenerEquipos();
          } catch (err) {
            console.error(err);
            alert("Error al eliminar el equipo");
          }
        }
      });

      const editar = document.createElement('button');
      editar.textContent = '✏️';
      editar.addEventListener('click', () => prepararEdicion(compu.id_equipo));

      const acciones = document.createElement('div');
      acciones.appendChild(editar);
      acciones.appendChild(eliminar);
      tarjetacompu.appendChild(acciones);
      contenedor.appendChild(tarjetacompu);
    });

    actualizarContadores();
  }

  function prepararEdicion(id) {
    const compu = computadoras.find(c => c.id_equipo === id);
    if (!compu) return;

    document.getElementById("TC").value = compu.tipo_equipo || "";
    document.getElementById("dueno").value = compu.nombre_dueno || "";
    document.getElementById("marca").value = compu.marca_compu || "";
    document.getElementById("procesador").value = compu.procesador || "";
    document.getElementById("gen").value = compu.generacion || "";
    document.getElementById("cram").value = compu.ram_cantidada || "";
    document.getElementById("TRAM").value = compu.tipo || "";
    document.getElementById("Cdisco").value = compu.almacenamiento_cantidad || "";
    document.getElementById("tipodisco").value = compu.almacenamiento_tipo || "";
    document.getElementById("MGPU").value = compu.grafica_modelo || "";
    document.getElementById("TGPU").value = compu.grafica_tipo || "";
    document.getElementById("pantalla").value = compu.tamanio_monitor || "";
    if(document.getElementById("estado")) document.getElementById("estado").value = compu.estado || "Operativo";
    
    idEditando = id;
    formElement.scrollIntoView({ behavior: 'smooth' });
  }

  function filtrarYBuscar() {
    const texto = busquedaInput ? busquedaInput.value.toLowerCase() : "";
    const estado = filtroEstado ? filtroEstado.value : "Todos";

    const resultados = computadoras.filter(compu => {
      const marca = compu.marca_compu || "";
      const dueno = compu.nombre_dueno || "";
      const coincideTexto = marca.toLowerCase().includes(texto) || dueno.toLowerCase().includes(texto);
      const coincideEstado = estado === "Todos" || (compu.estado || "Operativo") === estado;
      return coincideTexto && coincideEstado;
    });
    renderizarcomputadoras(resultados);
  }

  function actualizarContadores() {
    if (!contadoresContainer) return;
    const conteo = { Total: computadoras.length, Operativo: 0, "En reparación": 0, Descartado: 0 };
    computadoras.forEach(c => {
      const est = c.estado || "Operativo";
      if (conteo[est] !== undefined) conteo[est]++;
    });
    
    contadoresContainer.innerHTML = Object.entries(conteo)
      .map(([key, val]) => `<span><strong>${key}:</strong> ${val}</span>`)
      .join(" | ");
  }

  // MODO DÍA / NOCHE
  if (localStorage.getItem("tema") === "light") document.body.classList.add("light-mode");

  if (btnTema) {
    btnTema.addEventListener("click", () => {
      const esClaro = document.body.classList.toggle("light-mode");
      localStorage.setItem("tema", esClaro ? "light" : "dark");
    });
  }
});