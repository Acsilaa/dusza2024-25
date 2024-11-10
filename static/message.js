const messages_El = document.getElementById('messages');
const filter_El = document.getElementById('filterDiv');
const hasFilter = filter_El != null;

const filterToggle = document.getElementsByClassName("arrow")[0];

document.addEventListener('DOMContentLoaded', function(){
    filterToggle.classList.add("right")
    if(messages_El.innerHTML.indexOf("<li") === -1){
        messages_El.remove();
    }
    setTimeout(function(){
        messages_El.style.opacity = '0';
        messages_El.remove();
    },3000)

})
function showFilter(){
    if(filter_El.classList.contains('start-0')){
        filter_El.classList.remove('start-0');
        filterToggle.classList.remove("right")
        filterToggle.classList.add("left")


    }else{
        filter_El.classList.add('start-0');
        filterToggle.classList.remove("left")
        filterToggle.classList.add("right")
    }
}
function search(){

}

