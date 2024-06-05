// Add event listener to the arrival date input to calculate the minimim date for the departure input
let arrivalInput = document.getElementById('arrival');
let departureInput = document.getElementById('departure');

// Check if form inputs exist on current page
if (arrivalInput) {

    arrivalInput.addEventListener('change', function () {
        if (arrivalInput.value) {
            let arrivalDate = new Date(arrivalInput.value);
            let oneDayAfter = new Date();

            oneDayAfter.setDate(arrivalDate.getDate() + 1);

            let year = oneDayAfter.getFullYear();
            let month = ('0' + (oneDayAfter.getMonth() + 1)).slice(-2);
            let day = ('0' + oneDayAfter.getDate()).slice(-2);

            departureInput.min = `${year}-${month}-${day}`;
        }
    });
}