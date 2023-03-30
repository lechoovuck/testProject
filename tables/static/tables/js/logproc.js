const filterForm = document.getElementById('filterForm')
const filterButton = document.getElementById('filterButton')
const exportButton = document.getElementById('exportButton')
const loader = document.getElementsByClassName('loader')[0]

if ($('#proc').val().length > 0 ||
    $('#errorText').val().length > 0 ||
    $('#objType').val().length > 0 ||
    $('#errDtl').val().length > 0 ||
    ($('#id_eventtime_0').val().length > 0 &&
        $('#id_eventtime_1').val().length > 0)
) {
    exportButton.removeAttribute('disabled')
    filterButton.removeAttribute('disabled')
}
filterForm.addEventListener('input', () => {
    if ($('#proc').val().length > 0 ||
        $('#errorText').val().length > 0 ||
        $('#objType').val().length > 0 ||
        $('#errDtl').val().length > 0 ||
        ($('#id_eventtime_0').val().length > 0 &&
            $('#id_eventtime_1').val().length > 0)
    ) {
        exportButton.removeAttribute('disabled')
        filterButton.removeAttribute('disabled')
    } else {
        exportButton.setAttribute('disabled', 'disabled')
        filterButton.setAttribute('disabled', 'disabled')
    }
})
exportButton.addEventListener('click', () => {
    loader.classList.remove('loader-hidden')
})
filterButton.addEventListener('click', () => {
    loader.classList.remove('loader-hidden')
})