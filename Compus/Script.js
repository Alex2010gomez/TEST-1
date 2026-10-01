document.addEventListener("DOMContentLoaded", () => {
  const contenedor = document.getElementById("contenedor");
  const formulario = document.getElementById("submit");
  const busquedaInput = document.getElementById("busqueda");
  const filtroEstado = document.getElementById("filtroEstado");
  const contadoresContainer = document.getElementById("contadores");
  const btnExportar = document.getElementById("exportar");
  const btnImportar = document.getElementById("importar");

  let computadoras = JSON.parse(localStorage.getItem("compus")) || [];
  let indiceEditando = null;

  renderizarcomputadoras(computadoras);

  // Escuchar filtros en tiempo real
  if (busquedaInput) busquedaInput.addEventListener("input", filtrarYBuscar);
  if (filtroEstado) filtroEstado.addEventListener("change", filtrarYBuscar);

  // Evento Guardar / Editar
  formulario.addEventListener('submit', function (e) {
    e.preventDefault();
    const nuevacompu = {
      typecom: document.getElementById("TC").value,
      property: document.getElementById("dueno").value,
      brand: document.getElementById("marca").value,
      processor: document.getElementById("procesador").value,
      genprocessor: document.getElementById("gen").value,
      ramc: document.getElementById("cram").value,
      ramt: document.getElementById("TRAM").value,
      diskcapacity: document.getElementById("Cdisco").value,
      disktype: document.getElementById("tipodisco").value,
      marcagpu: document.getElementById("MGPU").value,
      tipogpu: document.getElementById("TGPU").value,
      screen: document.getElementById("pantalla").value,
      status: document.getElementById("estado").value // NUEVA PROPIEDAD: Estado
    };

    if (indiceEditando !== null) {
      computadoras[indiceEditando] = nuevacompu;
      indiceEditando = null;
    } else {
      computadoras.push(nuevacompu);
    }
    
    actualizarDatos(computadoras);
    formulario.reset();
  });

  function renderizarcomputadoras(listaAFiltrar = computadoras) {
    contenedor.innerHTML = "";
    listaAFiltrar.forEach((compu, indice) => {
      const tarjetacompu = document.createElement('div');
      tarjetacompu.classList.add('tarjeta-compu');
      tarjetacompu.innerHTML = `
        <h3>${compu.brand}</h3>
        <p>ID : ${indice + 1}</p>
        <p>Estado: <strong>${compu.status || 'Operativo'}</strong></p>
        <p>Tipo de computadora : ${compu.typecom}</p>
        <p>Dueño: ${compu.property}</p>
        <p>Marca del Procesador : ${compu.processor} </p>
        <p>Procesador : ${compu.genprocessor}</p>
        <p>RAM: ${compu.ramc}GB ${compu.ramt}</p>
        <p>Capacidad: ${compu.diskcapacity}GB ${compu.disktype}</p>
        <p>GPU: ${compu.marcagpu} ${compu.tipogpu}</p>
        <p>Pantalla de ${compu.screen} pulgadas</p>
      `;

      const eliminar = document.createElement('button');
      eliminar.textContent = '❌';
      eliminar.addEventListener('click', () => {
        computadoras.splice(indice, 1);
        actualizarDatos(computadoras);
      });

      const editar = document.createElement('button');
      editar.textContent = '✏️';
      editar.addEventListener('click', () => prepararEdicion(indice));

      const acciones = document.createElement('div');
      acciones.appendChild(editar);
      acciones.appendChild(eliminar);
      tarjetacompu.appendChild(acciones);
      contenedor.appendChild(tarjetacompu);
    });

    actualizarContadores();
  }

  function prepararEdicion(indice) {
    const compu = computadoras[indice];
    document.getElementById("TC").value = compu.typecom;
    document.getElementById("dueno").value = compu.property;
    document.getElementById("marca").value = compu.brand;
    document.getElementById("procesador").value = compu.processor;
    document.getElementById("gen").value = compu.genprocessor;
    document.getElementById("cram").value = compu.ramc;
    document.getElementById("TRAM").value = compu.ramt;
    document.getElementById("Cdisco").value = compu.diskcapacity;
    document.getElementById("tipodisco").value = compu.disktype;
    document.getElementById("MGPU").value = compu.marcagpu;
    document.getElementById("TGPU").value = compu.tipogpu;
    document.getElementById("pantalla").value = compu.screen;
    if(document.getElementById("estado")) document.getElementById("estado").value = compu.status || "Operativo";
    
    indiceEditando = indice;
    formulario.scrollIntoView({ behavior: 'smooth' });
  }

  // NUEVA FUNCIÓN: Combina Búsqueda por texto y Filtro de estado
  function filtrarYBuscar() {
    const texto = busquedaInput ? busquedaInput.value.toLowerCase() : "";
    const estado = filtroEstado ? filtroEstado.value : "Todos";

    const resultados = computadoras.filter(compu => {
      const coincideTexto = compu.brand.toLowerCase().includes(texto) || compu.property.toLowerCase().includes(texto);
      const coincideEstado = estado === "Todos" || (compu.status || "Operativo") === estado;
      return coincideTexto && coincideEstado;
    });
    renderizarcomputadoras(resultados);
  }

  // NUEVA FUNCIÓN: Calcula y muestra los contadores dinámicamente
  function actualizarContadores() {
    if (!contadoresContainer) return;
    const conteo = { Total: computadoras.length, Operativo: 0, "En reparación": 0, Descartado: 0 };
    computadoras.forEach(c => conteo[c.status || "Operativo"]++);
    
    contadoresContainer.innerHTML = Object.entries(conteo)
      .map(([key, val]) => `<span><strong>${key}:</strong> ${val}</span>`)
      .join(" | ");
  }

  // NUEVA FUNCIÓN: Helper para ahorrar líneas al actualizar localStorage y vista
  function actualizarDatos(nuevosDatos) {
    localStorage.setItem("compus", JSON.stringify(nuevosDatos));
    renderizarcomputadoras(nuevosDatos);
  }

  // NUEVAS FUNCIONES: Exportación e Importación JSON
  if (btnExportar) {
    btnExportar.addEventListener("click", () => {
      const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(computadoras, null, 2));
      const dlAnchorElem = document.createElement('a');
      dlAnchorElem.setAttribute("href", dataStr);
      dlAnchorElem.setAttribute("download", "computadoras.json");
      dlAnchorElem.click();
    });
  }

  if (btnImportar) {
    btnImportar.addEventListener("change", (e) => {
      const archivo = e.target.files[0];
      if (!archivo) return;
      const lector = new FileReader();
      lector.onload = (event) => {
        try {
          computadoras = JSON.parse(event.target.result);
          actualizarDatos(computadoras);
        } catch (err) {
          alert("Archivo JSON no válido");
        }
      };
      lector.readAsText(archivo);
    });
  }
    //  MODO DÍA / NOCHE
  const btnTema = document.getElementById("toggleTema");
  
  // Al cargar, verifica si ya existía una preferencia guardada
  if (localStorage.getItem("tema") === "light") document.body.classList.add("light-mode");

  if (btnTema) {
    btnTema.addEventListener("click", () => {
      // Intercambia la clase en el body
      const esClaro = document.body.classList.toggle("light-mode");
      // Guarda la elección para la próxima visita
      localStorage.setItem("tema", esClaro ? "light" : "dark");
    });
  }

});
