document.querySelectorAll('.product').forEach(product => {
    product.addEventListener('mouseover', () => {
        const choices = product.querySelector('.choices')
        if (choices) {
            choices.classList.add('active')
        }
    })

    product.addEventListener('mouseout', () => {
        const choices = product.querySelector('.choices')
        if (choices) {
            choices.classList.remove('active')
        }
    })
})

let search_bar = document.querySelector("nav #search-bar")

document.querySelector(".fa-search").addEventListener("click", ()=>{
    document.querySelector("nav form").submit()
})

document.querySelector(".close-btn").addEventListener("click", () => {
    document.querySelector(".sidebar").style.display = "none"
})

document.querySelector("#liked-container").addEventListener("click", () => {
    document.querySelector(".sidebar").style.display = "block"
})
