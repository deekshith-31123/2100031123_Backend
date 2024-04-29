// static/js/main.js
document.addEventListener('DOMContentLoaded', function () {
    const submitBtn = document.querySelector('.submit-btn');
    submitBtn.addEventListener('mouseover', function () {
        this.style.backgroundColor = '#0077c2'; // Darker blue when hovered
    });
    submitBtn.addEventListener('mouseout', function () {
        this.style.backgroundColor = '#29b6f6'; // Original color on mouse out
    });
});
