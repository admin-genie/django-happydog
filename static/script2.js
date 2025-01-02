document.addEventListener('DOMContentLoaded', function () {
    const customButtons = document.querySelectorAll('.custom-button');

    customButtons.forEach(button => {
        button.addEventListener('click', function () {
            this.classList.toggle('active'); 
        });
    });
});
