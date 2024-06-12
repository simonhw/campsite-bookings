let deleteButtons = document.getElementsByClassName("btn-delete");
let deleteConfirm = document.getElementById("deleteConfirm");

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let bookingId = e.target.getAttribute("booking_id");
        deleteConfirm.href = `delete/${bookingId}`;
    });
}
