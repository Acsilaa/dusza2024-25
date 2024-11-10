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
    layout += `#${cc} ${prev_end}% ${curr_end}%, `
    prev_end = curr_end
})
layout = layout.substring(0, layout.length - 2);

$("#pite").css('background', `conic-gradient(${layout})`)
console.log(datas,"asd")
for(i = 0; i < datas.length; i++){
    $(lga[i]).css('color',  `#${colors[i]}`)
    
}

