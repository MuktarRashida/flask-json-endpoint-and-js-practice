let btn = document.getElementById('btn')
let display = document.getElementById('box')

btn.addEventListener('click', async function displays()
{input = document.getElementById('txt').value
const response = await fetch ('/api/user')
    const data = await response.json()
    console.log(typeof data)
    console.log(data)
    display.textContent = data.name
})