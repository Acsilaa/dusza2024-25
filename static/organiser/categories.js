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
class Category
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
        this.htmlObject = $(obj).appendTo($(".categories.ajaxform"));
    }
    registerEventListeners(){
        let obj = this.htmlObject
        $($(obj).children("button")[0]).click(() => { //törlés
            let ajaxdata = {
                'category': this.name,
            }
            $.ajax({
                type: "post",
                url: "/category/remove/",
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
categories = []
cats.forEach(c => {
    categories.push(new Category(c))
});

$(".categories.ajaxform .adder .add").click(function(){
    let val = $(".categories.ajaxform .adder input").val()
    let ajaxdata = {
        "category": val
    }
    if(val.trim() == "")
        return
    $.ajax({
        type: "post",
        url: "/category/add/",
        data: ajaxdata,
        dataType: "json",
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken"),  // don't forget to include the 'getCookie' function
        },
        success: function (response) {
            if (response['result'] == "success"){
                categories.push(new Category(response['cat']))
                $(".categories.ajaxform .adder input").val("")
            }
        }
    });
})