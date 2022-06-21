cards = document.querySelectorAll('.card')

cards.forEach(card => {
    card.querySelector('.btn-floating').addEventListener('click', async _ => {
        console.log(card.dataset.json)
        try {
            const response = await fetch('/gallery/favourite/add', {
                method: 'post',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(card.dataset.json)
            });
            console.log('Completed!', response);
        } catch (err) {
            console.error(`Error: ${err}`);
        }
    })
});