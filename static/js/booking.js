let arrivalInput = document.getElementById('arrival');
let departureInput = document.getElementById('departure');

// Add event listener to the arrival date input so that the minimum date for the departure input is recalculate with each change.
arrivalInput.addEventListener('change', function () {
    if (arrivalInput.value) {
        let arrivalDate = new Date(arrivalInput.value);
        let oneDayAfter = new Date(arrivalDate);

        oneDayAfter.setDate(arrivalDate.getDate() + 1);

        // Split the date into its constituent components and increment month value by one.
        let year = oneDayAfter.getFullYear();
        let month = ('0' + (oneDayAfter.getMonth() + 1)).slice(-2);
        let day = ('0' + oneDayAfter.getDate()).slice(-2);

        departureInput.min = `${year}-${month}-${day}`;
    }
});
