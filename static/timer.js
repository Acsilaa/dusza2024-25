
const days = document.getElementById("days")
const hours = document.getElementById("hours")
const minutes = document.getElementById("minutes")
const sec = document.getElementById("seconds")


function timer(){
    
    const currentDate = new Date().getTime()
    const distance = targetDate - currentDate

    const Days = Math.floor(distance / 1000 / 60 / 60 / 24)
    const Hours = Math.floor(distance / 1000 / 60 / 60) % 24
    const Minutes = Math.floor(distance/ 1000/ 60) % 60
    const Seconds = Math.floor(distance/ 1000) % 60;

    days.innerText = Days
    hours.innerText = Hours
    minutes.innerText = Minutes
    sec.innerText = Seconds
    if (distance < 0){
        days.innerText = "00"
        hours.innerText = "00"
        minutes.innerText = "00"
        sec.innerText = "00"
    }
}

setInterval(timer, 1000)