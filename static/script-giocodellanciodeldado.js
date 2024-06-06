document.addEventListener("DOMContentLoaded", function () {
    // Aggiungi un listener per l'evento di click al pulsante
    document.getElementById("giocodellanciodeldado").addEventListener("submit", function (event) {
        // Mostra l'alert
        alert("Alea iacta est - Il dado è tratto (Giulio Cesare)");
        // Invia manualmente il form
        document.getElementById("giocodellanciodeldado").submit();
    });
});