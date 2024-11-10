const messages_El = document.getElementById('messages');
const filter_El = document.getElementById('filterDiv');

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
    const categories=document.getElementsByClassName('check_category');
    const languages=document.getElementsByClassName('check_language');
    const state_r=document.getElementsByClassName('check_r')[0];
    const state_i=document.getElementsByClassName('check_i')[0];
    const state_s=document.getElementsByClassName('check_s')[0];
    const contestant4=document.getElementsByClassName('check_p')[0];

    let filters = []
    //states
    if(state_r.checked||state_i.checked||state_s.checked){
        filters.push("?state=")
    }
    if(state_r.checked){
        filters[0] += "regisztralt;"
    }
    if(state_i.checked){
        filters[0] += "iskola altal jovahagyva;"
    }
    if(state_s.checked){
        filters[0] += "szervezok altal jovahagyva;"
    }
    //contestant4
    if(!contestant4.checked){
        filters.push("?contestant4=Nincs")
    }
    //categories
    for(let i = 0; i < categories.children.length; i++){
        if(categories.children[i].checked && filters.findIndex(function(item){
    return item.indexOf("?category=")!==-1;
}) === -1){
            filters.push("?category=")
        }
    }
    for(let i = 0; i < categories.children.length; i++){
        if(categories.children[i].checked){
            filters[filters.length-1]+=categories.children[i].getAttribute("name")+";";
        }
    }
    //languages
    for(let i = 0; i < languages.children.length; i++){
        if(languages.children[i].checked && filters.findIndex(function(item){
    return item.indexOf("?language=")!==-1;
}) === -1){
            filters.push("?language=")
        }
    }
    for(let i = 0; i < languages.children.length; i++){
        if(languages.children[i].checked){
            filters[filters.length-1]+=languages.children[i].getAttribute("name")+";";
        }
    }
    window.location.href = window.location.href+filters

}

