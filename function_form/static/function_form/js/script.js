const spinnerWrapperEl = document.querySelector('.spinner-wrapper');

setTimeout(() => {
    spinnerWrapperEl.style.opacity = '0';
    spinnerWrapperEl.remove();
}, 1000);