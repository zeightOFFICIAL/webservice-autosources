
                                // Navigation buttons logic



let mainPageBtn = document.querySelector('.navigation-main-page')
let userInputBtn = document.querySelector('.navigation-user-input')
let urlBtn = document.querySelector('.navigation-url')
let documentBtn = document.querySelector('.navigation-document')

let navBtnSet = document.querySelectorAll('.navigation-button')
console.log(navBtnSet)
let sections = document.querySelectorAll('section')
console.log(sections)

function deactivateBtns() {
    navBtnSet.forEach(button => {
        if (button.classList.contains('active')) {
            button.classList.remove('active')
        }
    })
}

function deactivateSections() {
    sections.forEach(section => {
        if (section.classList.contains('section-visible')) {
            section.classList.remove('section-visible')
        }
    })
}

navBtnSet.forEach(button => {
    button.addEventListener('click', () => {
        if (!button.classList.contains('active')) {
            deactivateBtns()
            deactivateSections()
            section = document.querySelector('.'+button.name)
            button.classList.add('active')
            section.classList.add('section-visible')
        }
    })
})



                                // Main page cards logic



let cards = document.querySelectorAll('.card')

cards.forEach(card => {
    card.addEventListener('click', () => {
        deactivateBtns()
        deactivateSections()
        button = document.querySelector('.'+card.getAttribute('name'))
        section = document.querySelector('.'+button.name)
        button.classList.add('active')
        section.classList.add('section-visible')
    })
})


                                // User input buttons logic



let userInpBtns = document.querySelectorAll('.user-input-button')
let userInpForms = document.querySelectorAll('.user-input-form')

userInpBtns.forEach(button => {
    button.addEventListener('click', () => {
        deactivateUserInpBtns()
        deactivateUserInpForms() 
        let bookForm = document.querySelector('.'+button.name)
        button.classList.add('user-input-active')
        bookForm.classList.add('form-visible')
    })
})

function deactivateUserInpBtns() {
    userInpBtns.forEach(button => {
        if (button.classList.contains('user-input-active')) {
            button.classList.remove('user-input-active')
        }
    })
}

function deactivateUserInpForms() {
    userInpForms.forEach(form => {
        if (form.classList.contains('form-visible')) {
            form.classList.remove('form-visible')
        }
    })
}
