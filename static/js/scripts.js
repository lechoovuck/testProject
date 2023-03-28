window.addEventListener('load', function () {
    var loader = document.querySelector('.loader');
    loader.classList.add('loader-hidden');
    loader.addEventListener('transitionend', function () {
        loader.remove();
    });
});
