panels = document.querySelectorAll('.panel')

panels.forEach(element => {
    element.onclick = () => {
        window.location.href = element.children[0].href;
    }
});