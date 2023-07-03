let menubar = document.querySelector('#menu-bars');
let mynav = document.querySelector('.navbar');



menubar.onclick = () =>{
    menubar.classList.toggle('fa-times');
    mynav.classList.toggle('active');
}
window.addEventListener('scroll', function() {
    var scrolled = window.pageYOffset;
    var background = document.querySelector('body');
    background.style.backgroundPosition = 'center ' + (-scrolled * 0.5) + 'px';
  });


