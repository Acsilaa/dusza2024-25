const lga = document.getElementsByClassName("lga");
const chart = document.getElementById("pite");
// datas
total = 0
Object.entries(datas).forEach(([key, value]) => {
    total += value*1
})
layout = ""
prev_end = 0
let colors =[]
Object.entries(datas).forEach(([key, value]) => {
    abc = "0123456789abcdef"
    cc = ""
    for(let i = 0; i<6; i++){
        cc += abc[Math.floor(Math.random() * abc.length)]
    }
    colors.push(cc)

    curr_end = Math.floor(value/total * 100)
    console.log(curr_end)
    layout += `#${cc} ${prev_end}% ${prev_end + curr_end}%, `
                        
                        
    $('ul.datas').append(`<li class="lga">${key}</li>`)
    prev_end += curr_end
})
layout = layout.substring(0, layout.length - 2);
console.log(layout)
$("#pite").css('background', `conic-gradient(${layout})`)
console.log(colors)
for(i = 0; i < colors.length; i++){
    $(lga[i]).css('color',  `#${colors[i]}`)
    
}

