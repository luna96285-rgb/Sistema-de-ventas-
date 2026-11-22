//Scrips js Para Funcionalidad del OJO en el campo de contraseñas para ver y ocultar contraseña.

document.querySelectorAll('.toggle-password').forEach(function (boton) {
  boton.addEventListener('click', function () {
    var campo = boton.closest('.password-wrap').querySelector('input');
    var icono = boton.querySelector('.ico');
    var oculto = campo.type === 'password';

    campo.type = oculto ? 'text' : 'password';
    icono.classList.toggle('ico-eye', !oculto);
    icono.classList.toggle('ico-eye-off', oculto);
    boton.setAttribute('aria-label', oculto ? 'Ocultar contraseña' : 'Mostrar contraseña');
  });
});