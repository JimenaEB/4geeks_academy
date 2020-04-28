var who = ["Angel", "Flor", "Juan", "Luis", "Sergio", "Mattia"];
var action =["ate", "broke", "destroyed", "burned"];
var what = ["my repositories", "the car", "the homework", "the server"];
var when = ["just on time", "yesterday", "durinh the class"];

window.onload = () => document.getElementById("excuse").innerHTML = getExcuse();

function getExcuse() {
    let phrase = [who, action, what, when];
    let excuse = ""

    for(sentence in phrase) {
        console.log();
        excuse = excuse.concat(" ", phrase[sentence][getRandom(phrase[sentence])]);
    }

    return excuse;
}

function getRandom(phrasePart) {
    return Math.floor(Math.random() * phrasePart.length);
}