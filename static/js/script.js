// Add event listener to the arrival date input to calculate the minimim date for the departure input
let arrivalInput = document.getElementById('arrival');
let departureInput = document.getElementById('departure');

// Check if form inputs exist on current page
if (arrivalInput) {

    arrivalInput.addEventListener('change', function () {
        console.log('arrivalInput was changed!');
        if (arrivalInput.value) {
            let arrivalDate = new Date(arrivalInput.value);
            console.log('arrivalDate is ', arrivalDate);
            let oneDayAfter = new Date(arrivalDate);

            oneDayAfter.setDate(arrivalDate.getDate() + 1);
            console.log('oneDayAfter is ', oneDayAfter);


            let year = oneDayAfter.getFullYear();
            console.log('year is ', year);
            let month = ('0' + (oneDayAfter.getMonth() + 1)).slice(-2);
            console.log('month is ', month);
            let day = ('0' + oneDayAfter.getDate()).slice(-2);
            console.log('day is ', day);

            departureInput.min = `${year}-${month}-${day}`;
            console.log('departureInput.min is ', departureInput.min);

        }
    });
}

let deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
let deleteButtons = document.getElementsByClassName("btn-delete");
let deleteConfirm = document.getElementById("deleteConfirm");

if (deleteModal) {

    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
        let bookingId = e.target.getAttribute("booking_id");
        deleteConfirm.href = `delete/${bookingId}`;
        });
    }
}
