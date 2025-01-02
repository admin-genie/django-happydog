document.addEventListener('DOMContentLoaded', function () {
    const fadeInElements = document.querySelectorAll('.fadeIn');
    const slideInElements = document.querySelectorAll('.slide-in');

    const checkInView = () => {
        fadeInElements.forEach(element => {
            const rect = element.getBoundingClientRect();
            const windowHeight = window.innerHeight;
            
            if (rect.top < windowHeight) {
                element.classList.add('active');
            }
        });

        slideInElements.forEach(element => {
            const rect = element.getBoundingClientRect();
            const windowHeight = window.innerHeight;
            
            if (rect.top < windowHeight * 0.8) {
                element.classList.add('active');
            } else {
                element.classList.remove('active');
            }
        });
    };

    window.addEventListener('scroll', checkInView);
    window.addEventListener('load', checkInView);
});
