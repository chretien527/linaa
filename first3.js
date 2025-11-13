const display = document.getElementById("display");

function appendtodisplay(input){
    display.value += input;
}

function calculate(){
    display.value = eval(display.value);
}

function cleardisplay(){
    display.value = "";
}
