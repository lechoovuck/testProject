const arrowDown = '<span class="material-icons-round arrow-sort">arrow_downward</span>'
const arrowUp = '<span class="material-icons-round arrow-sort">arrow_upward</span>'
const tableHeaders = document.getElementsByTagName('thead')[0]
                    .getElementsByTagName('tr')[0]
                    .getElementsByTagName('a')

for (let tableHeadersKey in tableHeaders) {
    let el = tableHeaders[tableHeadersKey]
    console.log(el)
    if (el.hasAttribute('sort')){
        if (el.getAttribute('sort') == 'asc')
            el.innerHTML += arrowUp
        else
            el.innerHTML += arrowDown
    }
}