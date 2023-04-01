function toggleAnswer(id) {
    var answer = document.getElementById("answer" + id);
    var plus = document.getElementById("plus" + id);
    var minus = document.getElementById("minus" + id);
    if (answer.style.display === "none") {
        answer.style.display = "block";
        plus.style.display = "none";
        minus.style.display = "inline-block";
    } else {
        answer.style.display = "none";
        plus.style.display = "inline-block";
        minus.style.display = "none";
    }
}
