/*GESTION DE TAREAS JEFATURA
**********************************************************************************/
(function(){
	// Variables
	var lista = document.getElementById("lista"),
		nombreTareaInput = document.getElementById("nombreTareaInput"),
		descripcionTarea = document.getElementById("descripcionTarea"),
		plazoTarea = document.getElementById("plazoTareaInput"),
		responsableTarea = document.getElementById("selectResponsable"),
		btnNuevaTarea = document.getElementById("btn-agregar");

	// Funciones
	var agregarTarea = function(){
		var nombreTarea = nombreTareaInput.value,
			descripcion = descripcionTarea.value,
			plazo = plazoTarea.value,
			responsable = responsableTarea.value,
			nuevaTarea = document.createElement("li"),
			enlace1 = document.createElement("a"),
			enlace2 = document.createElement("label"),
			enlace3 = document.createElement("label"),
			enlace4 = document.createElement("label"),
			salto1 = document.createElement("br"),
			salto2 = document.createElement("br"),
			contenido1 = document.createTextNode(nombreTarea),
			contenido2 = document.createTextNode(descripcion),
			contenido3 = document.createTextNode(plazo),
			contenido4 = document.createTextNode(responsable);

		if (nombreTarea === "") {
			nombreTareaInput.setAttribute("placeholder", "Debe ingresar un nombre de tarea...");
			nombreTareaInput.className = "error"; // Si esta vacio le asignamos la clase error
			return false;
		}

		// Agregamos el contenido al enlace
		enlace1.appendChild(contenido1);
		enlace2.appendChild(contenido2);
		enlace3.appendChild(contenido3);
		enlace4.appendChild(contenido4);
		// Le establecemos un atributo href
		enlace1.setAttribute("href", "#");
		// Agrergamos el enlace (a) a la nueva tarea (li)
		nuevaTarea.appendChild(enlace1);
		nuevaTarea.appendChild(enlace2);
		nuevaTarea.appendChild(salto1);
		nuevaTarea.appendChild(enlace3);
		nuevaTarea.appendChild(salto2);
		nuevaTarea.appendChild(enlace4);
		// Agregamos la nueva tarea a la lista
		lista.appendChild(nuevaTarea);

		nombreTareaInput.value = "";
		descripcionTarea.value = "";

		for (var i = 0; i <= lista.children.length -1; i++) {
			lista.children[i].addEventListener("click", function(){
				this.parentNode.removeChild(this);
			});
		}

	};
	var comprobarInput = function(){
		nombreTareaInput.className = "";
		nombreTareaInput.setAttribute("placeholder", "Ingrese un nombre");
	};

	var eliminarTarea = function(){ // Funcion para eliminar tarea
		this.parentNode.removeChild(this);
	};

	// Eventos

	// Agregar Tarea
	btnNuevaTarea.addEventListener("click", agregarTarea);

	// Comprobar Input
	nombreTareaInput.addEventListener("click", comprobarInput);
	
	// Borrando Elementos de la lista
	for (var i = 0; i <= lista.children.length -1; i++) {
		lista.children[i].addEventListener("click", eliminarTarea);
	}
}());