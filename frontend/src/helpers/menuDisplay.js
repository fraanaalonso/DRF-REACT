const hamburguerContainer = document.querySelector('#header__main-nav');
const hamburger = document.querySelector('.header__main-nav--hamburger');
const links = document.querySelectorAll('.header__main-nav--links li')



hamburger.addEventListener('click', () => {
    hamburguerContainer.classList.toggle('clicked'); /*we add this class to the container to manage the vertical menu*/
    
    links.forEach((link) => {
        link.classList.toggle('fade');
    })
    
})