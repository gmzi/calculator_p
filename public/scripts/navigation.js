const currentUrl = window.location.href;
const BASE_URL = `${window.origin}/`;

console.log('origin: ')
console.log(origin)

function extractUrlPart() {
    const origin = window.location.origin;
    const extensionIndex = currentUrl.indexOf(".")
    const startIndex = BASE_URL.length
    const endIndex = extensionIndex
    const urlPart = currentUrl.substring(startIndex, endIndex)
    return urlPart
}

function makeActive() {
    let urlPart = extractUrlPart()
    const navLinks = document.querySelectorAll('nav ul li a')

    navLinks.forEach(function (link) {
        const attr = link.getAttribute('href')
        if (attr === '/' && urlPart === BASE_URL) {
            link.classList.add('active-page');
        } else if (attr.includes(urlPart)) {
            link.classList.add('active-page');
        } else {
            link.classList.remove('active-page');
        }
    })
}

document.addEventListener('DOMContentLoaded', function () {
    makeActive();
});