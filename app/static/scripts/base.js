if (window.NodeList && !NodeList.prototype.map) {
    NodeList.prototype.map = Array.prototype.map;
}

const flashes = document
    .querySelectorAll('.flashed-message')
    .map(message_container => message_container.dataset)

function getColor(category) {
    let color = "red";
    switch (category) {
        case 'success':
            color = 'green'
            break;
        case 'info':
            color = 'blue'
            break;
        case 'warning':
            color = 'yellow'
            break;
        case 'danger':
            color = 'red'
            break;
    }
    return color
}

window.addEventListener('load', (event) => {
    flashes.forEach(flash => {
        M.toast({ html: flash.message, classes: getColor(flash.category) })
    })
})