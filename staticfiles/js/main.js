// Start Add Comment
document.addEventListener('DOMContentLoaded', function () {
    var addCommentBtn = document.getElementById('addCommentBtn');
    var usernameInput = document.getElementById('usernameInput');
    var commentInput = document.getElementById('commentInput');
    var commentsContainer = document.getElementById('commentsContainer');
    
    addCommentBtn.addEventListener('click', function () {
        var username = usernameInput.value;
        var comment = commentInput.value;
        
        if (username && comment) {
            saveComment(username, comment);
            usernameInput.value = '';
            commentInput.value = '';
            displayComments();
        }
    });
    
    function saveComment(username, comment) {
        var comments = localStorage.getItem('comments');
        comments = comments ? JSON.parse(comments) : [];
        
        var newComment = {
            username: username,
            comment: comment,
            likes: 0,
            dislikes: 0
        };
        
        comments.push(newComment);
        localStorage.setItem('comments', JSON.stringify(comments));
    }
    
    function displayComments() {
        var comments = localStorage.getItem('comments');
        comments = comments ? JSON.parse(comments) : [];
        
        var html = '';
        
        for (var i = 0; i < comments.length; i++) {
            var comment = comments[i];
            var likes = comment.likes;
            var dislikes = comment.dislikes;
            
            html += '<div class="comment">';
            html += '<div class="username">' + comment.username + '</div>';
            html += '<div class="comment-text">' + comment.comment + '</div>';
            html += '<div class="likes' + (likes > 0 ? ' active' : '') + '" onclick="likeComment(' + i + ')"><i class="fa fa-thumbs-up"></i> ' + likes + '</div>';
            html += '<div class="dislikes' + (dislikes > 0 ? ' active' : '') + '" onclick="dislikeComment(' + i + ')"><i class="fa fa-thumbs-down"></i> ' + dislikes + '</div>';
            html += '</div>';
        }
        
        commentsContainer.innerHTML = html;
    }
    
    window.likeComment = function (index) {
        var comments = localStorage.getItem('comments');
        comments = comments ? JSON.parse(comments) : [];
        
        var comment = comments[index];
        
        if (comment.likes <= 0) {
            comment.likes++; // =1
            comment.dislikes = 0;
        } else {
            comment.likes = 0;
        }
        
        localStorage.setItem('comments', JSON.stringify(comments));
        displayComments();
    };
    
    window.dislikeComment = function (index) {
        var comments = localStorage.getItem('comments');
        comments = comments ? JSON.parse(comments) : [];
        
        var comment = comments[index];
        
        if (comment.dislikes <= 0) {
            comment.likes = 0;
            comment.dislikes++; // =1
        } else {
            comment.dislikes = 0;
        }
        
        localStorage.setItem('comments', JSON.stringify(comments));
        displayComments();
    };
    
    displayComments();
});
// End Add Comment
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
// Start Order
document.addEventListener('DOMContentLoaded', function() {

    const removeButtons = document.querySelectorAll('.remove-btn');
    
    removeButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            const card = button.closest('.card-content'); 
            if (card) {
                Swal.fire({
                    title: 'Are you sure to delete this product?',
                    icon: 'question',
                    showCancelButton: true,
                    confirmButtonText: 'Yes',
                    cancelButtonText: 'No'
                }).then((result) => {
                    if (result.isConfirmed) {
                        card.remove();
                    } 
                });
            }
        });
    });

const quantityContainers = document.querySelectorAll('.quantity-container');

quantityContainers.forEach(function (container) {
    const minusBtn = container.querySelector('.minus-btn');
    const plusBtn = container.querySelector('.plus-btn');
    const quantityInput = container.querySelector('.quantity-input');

    minusBtn.addEventListener('click', function () {
        let currentValue = parseInt(quantityInput.value);
        if (currentValue > 1) {
        quantityInput.value = currentValue - 1;
    }
    updateButtonStates();
});

    plusBtn.addEventListener('click', function () {
    let currentValue = parseInt(quantityInput.value);
    quantityInput.value = currentValue + 1;
    updateButtonStates();
});

    function updateButtonStates() {
    const currentValue = parseInt(quantityInput.value);
    minusBtn.disabled = currentValue === 1;
    plusBtn.disabled = currentValue > 5;
}
});

    const currentLocationLink = document.getElementById("currentLocation");
    currentLocationLink.addEventListener("click", function(event) {
        // تجنب فتح الرابط الأصلي
        event.preventDefault();
        const form = document.getElementById('formLocation');
        form.style.display = 'none';
        const formFields = formLocation.querySelectorAll(".inp");
        formFields.forEach(field => {
            field.required = false;
            field.value = "";
        });
    });
    
    document.getElementById('toggleForm').addEventListener('click', function() {
        const showCurrentLocation = document.getElementById('showCurrentLocation');
        showCurrentLocation.style.display = 'none';
        const label = document.getElementById('label');
        label.style.display = 'none';
        const form = document.getElementById('formLocation');
        const locationInput = document.getElementById('locationInput');
        if (form.style.display === 'none' || form.style.display === '') {
            form.style.display = 'block';
        } else {
            form.style.display = 'none';
        }
        locationInput.value = "";
        const formFields = formLocation.querySelectorAll(".inp");
        formFields.forEach(field => {
            field.required = true;
        });
    });

    const formLocation = document.getElementById("formLocation");
    const locationInput = document.getElementById("locationInput");
    const getLocationBtn = document.getElementById("currentLocation");

        getLocationBtn.addEventListener("click", function() {
            // start geolocation
            // get coordinates from geolocation
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(
                    function(position) {
                        const latitude = position.coords.latitude;
                        const longitude = position.coords.longitude;
                        // start open weather map
                        // convert coordinates to names from open weather map
                        const url = `http://api.openweathermap.org/geo/1.0/reverse?lat=${latitude}&lon=${longitude}&limit=1&appid=be79259c7f73c5a62a79c8df9d89d435`
    
                        async function get_location(url){
                            const res = await fetch(url)
                            const data = await res.json(); 
                            
                            const country = data[0].country; 
                            const state = data[0].state;
                            const city = data[0].name;
                    
                            locationInput.value = `${country} - ${state} - ${city}`;
                            var val = locationInput.value;
                            showCurrentLocation.style.display = 'block';
                            showCurrentLocation.innerHTML = val;
                            label.style.display = 'block';
                        }
                        get_location(url)
                        // end open weather map

                        Swal.fire({
                            title: "Good job!",
                            text: "Location retrieved successfully, Confirm order now",
                            icon: "success"
                        });
                    },
                    function(error) {
                        if (error.code === error.PERMISSION_DENIED) {
                            Swal.fire({
                                title: "Sorry!",
                                text: "Access to location was blocked. Please allow access to proceed.",
                                icon: "error"
                            });
                            const locationInput = document.getElementById('locationInput');
                            locationInput.required = true;
                            const formFields = formLocation.querySelectorAll(".inp");
                            formFields.forEach(field => {
                                field.required = true;
                            });
                            showCurrentLocation.style.display = 'none';
                            showCurrentLocation.innerHTML = '';
                            label.style.display = 'none';
                            return;
                        }
                    }
                );
            } else {
                Swal.fire({
                    title: "Sorry!",
                    text: "Geolocation is not supported by your browser.",
                    icon: "error"
                });
            }
            // end geolocation
        });
});
// End Order


