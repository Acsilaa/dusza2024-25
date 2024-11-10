const messages_El = document.getElementById('messages');
const filter_El = document.getElementById('filterDiv');

const filterToggle = document.getElementsByClassName("arrow")[0];

document.addEventListener('DOMContentLoaded', function(){
    const categories=document.getElementsByClassName('check_category');
    if(categories.length > 0) {
        initFilters()
    }
    if(messages_El.innerHTML.indexOf("<li") === -1){
        messages_El.remove();
    }
    setTimeout(function(){
        messages_El.style.opacity = '0';
        messages_El.remove();

    },3000)


})
function initFilters(){
    const categories=document.getElementsByClassName('check_category');
    const languages=document.getElementsByClassName('check_language');
    const state_r=document.getElementsByClassName('check_r')[0];
    const state_i=document.getElementsByClassName('check_i')[0];
    const state_s=document.getElementsByClassName('check_s')[0];
    const contestant4=document.getElementsByClassName('check_p')[0];
    const contestant4_contains=document.getElementsByClassName('check_p_c')[0];
    const params = new Proxy(new URLSearchParams(window.location.search), {
      get: (searchParams, prop) => searchParams.get(prop),
    });
    if(params.category ||params.language ||params.contestant4 ||params.state){
        filter_El.classList.add('start-0');
        filter_El.style.transition = 'none';
        filterToggle.classList.remove("left")
        filterToggle.classList.add("right")
        setTimeout(()=>{
            filter_El.style.transition = 'ease-in-out .5s';
        },100)

    }else{
        filterToggle.classList.add("left")
        return
    }
    state_r.checked=false
    state_i.checked=false
    state_s.checked=false
    if(params.state){
        let state_params = params.state.split(";").slice(0,params.state.split(";").length-1)
        if(state_params.indexOf("regisztralt") !== -1){
            state_r.checked=true
        }
        if(state_params.indexOf("iskola altal jovahagyva") !== -1){
            state_i.checked=true
        }
        if(state_params.indexOf("szervezok altal jovahagyva") !== -1){
            state_s.checked=true
        }
    }
    contestant4.checked=false
    contestant4_contains.checked=false
    if(params.contestant4){
        if(params.contestant4 === "Van"){
            contestant4_contains.checked=true
        }
    }else{
        contestant4.checked=true
    }

    for(let i=0;i<categories.length;i++){
        categories[i].checked = false;
    }
    if(params.category){
        let categories_params=params.category.split(";").slice(0,params.category.split(";").length-1)
        for (let i =0;i<categories_params.length;i++){
            for(let j = 0;j<categories.length;j++){
                if(categories[j].getAttribute("name")===categories_params[i]){
                    categories[j].checked=true;
                }
            }
        }
    }
    for(let i=0;i<languages.length;i++){
        languages[i].checked = false;
    }
    if(params.language){
        let languages_params=params.language.split(";").slice(0,params.language.split(";").length-1)
        for (let i =0;i<languages_params.length;i++){
            for(let j = 0;j<languages.length;j++){
                if(languages[j].getAttribute("name")===languages_params[i]){
                    languages[j].checked=true;
                }
            }
        }
    }
}
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
function contestant4(){
    const contestant4=document.getElementsByClassName('check_p')[0];
    const contestant4_contains=document.getElementsByClassName('check_p_c')[0];
    if(contestant4.checked){
        
    }
}

function search(){
    const categories=document.getElementsByClassName('check_category');
    const languages=document.getElementsByClassName('check_language');
    const state_r=document.getElementsByClassName('check_r')[0];
    const state_i=document.getElementsByClassName('check_i')[0];
    const state_s=document.getElementsByClassName('check_s')[0];
    const contestant4=document.getElementsByClassName('check_p')[0];
    const contestant4_contains=document.getElementsByClassName('check_p_c')[0];

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
    filters[0]+="&"
    //contestant4
    if(!contestant4.checked){
        if(contestant4_contains.checked){
            filters.push("contestant4=Van")
            filters[filters.length-1]+="&"
        }else{
            filters.push("contestant4=Nincs")
            filters[filters.length-1]+="&"
        }

    }

    //categories
    filters.push("category=")
    for(let i = 0; i < categories.length; i++){
        if(categories[i].checked){
            filters[filters.length-1]+=categories[i].getAttribute("name")+";";
        }
    }
    filters[filters.length-1]+="&"
    //languages
    filters.push("language=")
    for(let i = 0; i < languages.length; i++){
        if(languages[i].checked){
            filters[filters.length-1]+=languages[i].getAttribute("name")+";";
        }
    }
    filters[filters.length-1]+="&"
    window.location.href = location.protocol + '//' + location.host + location.pathname+filters.join("")


}

function toggleCheckbox() {
    const contains = document.getElementById("tartalmazza");
    const all = document.getElementById("all");
    if (all.checked) {
        contains.checked = false;
    }

}
