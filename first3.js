const display = document.getElementById("display");
const createElement = document.createElement('h1')

function appendtodisplay(input){
    display.value += input;
}

function calculate(){
    display.value = eval(display.value);
}

function cleardisplay(){
    display.value = "";
}
