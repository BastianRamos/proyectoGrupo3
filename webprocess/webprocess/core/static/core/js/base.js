// Cuando el usuario haga scroll, la funcion se activa
window.onscroll = function() {navBarPegajoso()};

// Tomamos el navbar
var navbar = document.getElementById("navbar");

// Posicion del navbar
var sticky = navbar.offsetTop;

// Agreagamos la clase sticky cuando se realiza el desplazamiento del navbar
function navBarPegajoso() {
    if (window.pageYOffset >= sticky) {
        navbar.classList.add("sticky")
    } else {
        navbar.classList.remove("sticky");
    }
}