const messages_El = document.getElementById('messages');
const filter_El = document.getElementsByClassName('filter')[0];
const hasFilter = filter_El != null;

document.addEventListener('DOMContentLoaded', function(){
    if(messages_El.innerHTML.indexOf("<li") === -1){
        messages_El.remove();
    }
    setTimeout(function(){
        messages_El.style.opacity = '0';
        messages_El.remove();
    },3000)
    filter_El.classList.add('start-0');

})
function showFilter(){
    if(filter_El.classList.contains('start-0')){
        filter_El.classList.remove('start-0');
    }else{
        filter_El.classList.add('start-0');
    }
}
function search(){

}

