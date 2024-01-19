// Add Rating
document.addEventListener("DOMContentLoaded", function() {
    const stars = document.querySelectorAll('.star');
    const ratingInput = document.getElementById('ratingInput');
    let selectedRating = 0;

stars.forEach(star => {
    star.addEventListener('click', () => {
        const value = star.getAttribute('data-value');
        selectedRating = value;
        setRating(selectedRating);
    });
});

    function setRating(value) {
        stars.forEach(star => {
        star.classList.remove('active');
    });

    for (let i = 0; i < value; i++) {
        stars[i].classList.add('active');
    }

    // قم بتعيين قيمة النجمة في الـ input الخفي
    ratingInput.value = value;
}
});
// End Rating