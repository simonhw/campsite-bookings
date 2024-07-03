let deleteButtons = document.getElementsByClassName("btn-delete");

// Loop through each delete button and assign the correct booking id to its href attribute.
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let bookingId = e.target.getAttribute("data-booking_id");
        let deleteConfirm = document.getElementById("deleteConfirm");
        deleteConfirm.href = `delete/${bookingId}`;
    });
}
