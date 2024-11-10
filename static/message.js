const messages_El = document.getElementById('messages');
const filter_El = document.getElementsByClassName('filter')[0];


document.addEventListener('DOMContentLoaded', function(){
    if(messages_El.innerHTML.indexOf("<li") === -1){
        messages_El.remove();
    }
    setTimeout(function(){
        messages_El.style.opacity = '0';
        messages_El.remove();
    },3000)
    console.log(filter_El);
    filter_El.classList.add('start-0');

})

