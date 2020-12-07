/*ACCEDE A TODOS LOS INPUTS Y DEVUELVE UN ARRAY CON ELLOS
**********************************************************************************/
const inputs = document.querySelectorAll(".input");

function addcl(){
	let parent = this.parentNode.parentNode;
	parent.classList.add("focus");
}

function remcl(){
	let parent = this.parentNode.parentNode;
	if(this.value == ""){
		parent.classList.remove("focus");
	}
}

inputs.forEach(input => {
	input.addEventListener("focus", addcl);
	input.addEventListener("blur", remcl);
});

/*VALIDACIÓN DE USUARIO
************************************************************************************/
function validarCuenta()
{
	var user = document.getElementById('nombreUsuario').value;
	var pass = document.getElementById('password').value;
	var regexUser = /^[a-z]/;
	var regexPass = /^\d+/;

	if(user.length < 4)
	{
		alert('Nombre de usuario demasiado corto. Tamaño mínimo 4.');
		return false;
	}
	if(user.length > 15)
	{
		alert('Nombre de usuario demasiado extenso. Tamaño máximo 15.');
		return false;
	}
	if(!regexUser.test(user))
	{
		alert('Nombre de usuario no válido. Ingrese sólo letras.');
		return false;
	}
	if(pass.length < 4)
	{
		alert('La contraseña es demasiada corta. Tamaño mínimo de 4 dígitos.');
		return false;
	}
	if(pass.length > 6)
	{
		alert('La contraseña es demasiada extensa. Tamaño máximo de 6 dígitos.');
		return false;
	}
	if(!regexPass.test(pass))
	{
		alert('La contraseña sólo puede contener números.');
		return false;
	}
}