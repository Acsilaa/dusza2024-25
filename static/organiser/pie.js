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
function inarray(arr, e){
    for(i = 0; i < arr.length; i++){
        if(e == arr[i])
            return true
    }
    return false
}
it = 0
_colors = [
    "22577a",
    "38a3a5",
    "57cc99",
    "80ed99",
    "c7f9cc",
    "FFFFFC",
    "757780",
    "D5ACA9",
    "0892A5",
    "BB7E5D",
    "CE4760",
    "6369D1",
    "34435E",
    "60E1E0"
];
Object.entries(datas).forEach(([key, value]) => {
    index = Math.floor(Math.random() * _colors.length)
    console.log(index)
    cc = _colors[it]

    curr_end = Math.floor(value/total * 100)
    layout += `#${cc} ${prev_end}% ${prev_end + curr_end}%, `
                        
    colors.push(cc)
    $('ul.datas').append(`<li class="lga">${key}</li>`)
    prev_end += curr_end
    it++
})
layout = layout.substring(0, layout.length - 2);
$("#pite").css('background', `conic-gradient(${layout})`)
console.log(colors)
for(i = 0; i < colors.length; i++){
    $(lga[i]).css('color',  `#${colors[i]}`)
    
}

