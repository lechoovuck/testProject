$('.modal-button').click((el) => {
    let id = el.target.getAttribute('targetModal')
    $(id).css('display', 'block')
    $(id).css('transform', 'translateX(0px)')
    $('.modal-close').click(() => {
        $(id).css('display', 'none')
        $(id).css('transform', 'translateX(-100%)')
    })

})

