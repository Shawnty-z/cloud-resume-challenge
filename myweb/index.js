const counter = document.querySelector(".counter-number");
async function updateCounter() {
    let response = await fetch("https://0lgtwmuvr7.execute-api.eu-west-2.amazonaws.com/Prod/views");
    let data = await response.json();
    counter.innerHTML = "views: " + data.count;
}
updateCounter()