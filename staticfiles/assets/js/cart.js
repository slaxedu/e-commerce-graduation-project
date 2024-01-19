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
    const formFields = formLocation.querySelectorAll(".inp");
    formFields.forEach(field => {
        field.required = false;
        field.value = "";
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
                            
                            Swal.fire({
                            title: "Good job!",
                            text: "Location retrieved successfully, Confirm order now",
                            icon: "success"
                            });
                            locationInput.value = `${country} - ${state} - ${city}`;
                            var val = locationInput.value;
                            showCurrentLocation.style.display = 'block';
                            showCurrentLocation.innerHTML = val;
                            label.style.display = 'block';
                        }
                        get_location(url)
                        // end open weather map
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