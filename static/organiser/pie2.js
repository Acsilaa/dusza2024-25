const lga2 = document.getElementsByClassName("lga2");
const chart2 = document.getElementById("pite");
// datas2
total = 0
Object.entries(datas2).forEach(([key, value]) => {
    total += value*1
})
layout = ""
prev_end = 0
colors =[]
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
Object.entries(datas2).forEach(([key, value]) => {
    index = Math.floor(Math.random() * _colors.length)
    console.log(index)
    cc = _colors[it]

    curr_end = Math.floor(value/total * 100)
    layout += `#${cc} ${prev_end}% ${prev_end + curr_end}%, `
                        
    colors.push(cc)
    $('ul.datas2').append(`<li class="lga2">${key}</li>`)
    prev_end += curr_end
    it++
})
layout = layout.substring(0, layout.length - 2);
$("#pite2").css('background', `conic-gradient(${layout})`)
for(i = 0; i < colors.length; i++){
    $(lga2[i]).css('color',  `#${colors[i]}`)
    
}