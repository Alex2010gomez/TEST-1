document.addEventListener("DOMContentLoaded", () => {
    const contenedor = document.getElementById("contenedor");
    const formulario = document.getElementById("submit");

  // Input del filtro 
    const busquedaInput = document.getElementById("busqueda");

    let computadoras = JSON.parse(localStorage.getItem("compus")) || [];
    let indiceEditando = null; //marca si se esta editando

  // Renderizar al cargar la página
    renderizarcomputadoras(computadoras);

  // Escuchar el input de búsqueda en tiempo real
    if (busquedaInput) {
        busquedaInput.addEventListener("input", filtrar);
    }

    formulario.addEventListener('submit', function (e) {
    e.preventDefault();//evita que se recargue o cierre si el formulario tiene datos no entregados 

    const nuevacompu = { // se guarda en un array todo lo que se va a agregar al json 
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
        screen: document.getElementById("pantalla").value
    };

    if (indiceEditando !== null) {
      // Si estamos editando, reemplazamos el elemento en el índice correspondiente
        computadoras[indiceEditando] = nuevacompu;
      indiceEditando = null; // Reseteamos el estado de edición
    } else {
      // Si no, agregamos una nueva
        computadoras.push(nuevacompu);
    }

    localStorage.setItem("compus", JSON.stringify(computadoras));
    formulario.reset();
    renderizarcomputadoras(computadoras);
    });

  // Enves de recibir haci no mas tambien puede recibir un array para no alargar demasiado 
    function renderizarcomputadoras(listaAFiltrar = computadoras) {
        contenedor.innerHTML = "";

        listaAFiltrar.forEach((compu, indice) => {
        const tarjetacompu = document.createElement('div');
        tarjetacompu.classList.add('tarjeta-compu');

        tarjetacompu.innerHTML = `
            <h3>${compu.brand}</h3>
            <p>ID : ${indice + 1}</p>
            <p>Tipo de computadora : ${compu.typecom}</p>
            <p>Dueño: ${compu.property}</p>
            <p>Marca del Procesador : ${compu.processor} </p>
            <p>Procesador : ${compu.genprocessor}</p>
            <p>RAM: ${compu.ramc}GB ${compu.ramt}</p>
            <p>Capacidad: ${compu.diskcapacity}GB ${compu.disktype}</p>
            <p>GPU: ${compu.marcagpu} ${compu.tipogpu}</p>
            <p>Pantalla de ${compu.screen} pulgadas</p>
        `;

      // Botón Eliminar
        const eliminar = document.createElement('button');
        eliminar.textContent = '❌';
        eliminar.addEventListener('click', () => {
        computadoras.splice(indice, 1);
        localStorage.setItem('compus', JSON.stringify(computadoras));
        renderizarcomputadoras(computadoras);
        });

      // Botón Editar
        const editar = document.createElement('button');
        editar.textContent = '✏️';
        editar.addEventListener('click', () => {
        prepararEdicion(indice);
        });

      // Contenedor para los botones de acción
        const acciones = document.createElement('div');
        acciones.appendChild(editar);
        acciones.appendChild(eliminar);
        
        tarjetacompu.appendChild(acciones);
        contenedor.appendChild(tarjetacompu);
    });
    }

  // Función para cargar los datos en el formulario
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

    // Guardamos el índice global que estamos editando
    indiceEditando = indice;
    
    // Hace scroll hacia el formulario para avisar al usuario
    formulario.scrollIntoView({ behavior: 'smooth' });
    }

  // Función de filtrado 
    function filtrar() {
    let busqueda = document.getElementById("busqueda").value;
    let elementoabuscar = busqueda.toLowerCase();

    const resultados = computadoras.filter(compu => {
        const marcacoin = compu.brand.toLowerCase().includes(elementoabuscar);
        const duenocon = compu.property.toLowerCase().includes(elementoabuscar);
        return marcacoin || duenocon;
    });

    renderizarcomputadoras(resultados);
    }
});
