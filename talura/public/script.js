const cards = document.querySelectorAll('.clientes .card');
const prev = document.querySelector('.seta-esq');
const next = document.querySelector('.seta-dir');
let activeIndex = 0;

function updateCards() {
    cards.forEach((card, i) => {
        card.classList.toggle('active', i === activeIndex);
    });
}

next.addEventListener('click', () => {
    activeIndex = (activeIndex + 1) % cards.length;
    updateCards();
});

prev.addEventListener('click', () => {
    activeIndex = (activeIndex - 1 + cards.length) % cards.length;
    updateCards();
});

updateCards();