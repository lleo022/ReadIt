function validateForm() {
    const title = document.getElementById("title").value.trim();
    const genre = document.getElementById("genre").value.trim();

    if (title === "" && genre === "") {
        alert("Please fill in at least one field (Title or Genre).");
        return false;
    }
    return true;
}

