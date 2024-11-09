function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + "=")) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
class Language
{
    name;
    htmlObject;
    constructor(name){
        
        this.name = name
        this.createElement()
        this.registerEventListeners()
    }
    createElement(){
        let obj = `<div class="ajaxitem">
                    <span>${this.name}</span>
                    <button class="delete">Törlés</button>
                </div>`;
        this.htmlObject = $(obj).appendTo($(".languages.ajaxform"));
    }
    registerEventListeners(){
        let obj = this.htmlObject
        $($(obj).children("button")[0]).click(() => { //törlés
            let ajaxdata = {
                'language': this.name,
            }
            $.ajax({
                type: "post",
                url: "/language/remove/",
                data: ajaxdata,
                dataType: "json",
                headers: {
                    "X-Requested-With": "XMLHttpRequest",
                    "X-CSRFToken": getCookie("csrftoken"),  // don't forget to include the 'getCookie' function
                },
                success: (response) => {
                    if(response['result'] == "success"){
                        $($(this.htmlObject)).remove();
                    }
                }
            });
        })
    }
}
languages = []
langs.forEach(c => {
    languages.push(new Language(c))
});

$(".languages.ajaxform .adder .add").click(function(){
    let val = $(".languages.ajaxform .adder input").val()
    let ajaxdata = {
        "language": val
    }
    
    if(val.trim() == ""){
        return
    }
    $.ajax({
        type: "post",
        url: "/language/add/",
        data: ajaxdata,
        dataType: "json",
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken"),  // don't forget to include the 'getCookie' function
        },
        success: function (response) {
            console.log(response)
            if (response['result'] == "success"){
                languages.push(new Language(response['lang']))
                $(".languages.ajaxform .adder input").val("")
            }
        }
    });
})