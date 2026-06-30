let btn = document.getElementById('btn')
let display = document.getElementById('box')

if (btn){btn.addEventListener('click', async function displays()
{const response = await fetch ('/api/user')
    const data = await response.json()
    console.log(typeof data)
    console.log(data)
    display.textContent = data.name
})}

let btn2 = document.getElementById('btn2')
let display2 = document.getElementById('box2')

if (btn2){btn2.addEventListener('click', async function displays()
{input2 = document.getElementById('txt2').value
const response = await fetch ('/api/role?names=' + input2)
    const data = await response.json()
    console.log(typeof data)
    console.log(data)
    display2.textContent = data.result
})}