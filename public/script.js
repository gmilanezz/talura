document.addEventListener("DOMContentLoaded", () => {
    const container = document.querySelector(".depoimentos");
    const setaEsq = document.getElementById("seta-esq");
    const setaDir = document.getElementById("seta-dir");

    setaDir.addEventListener("click", () => {
        container.scrollLeft += 300;
    });

    setaEsq.addEventListener("click", () => {
        container.scrollLeft -= 300;
    });
});