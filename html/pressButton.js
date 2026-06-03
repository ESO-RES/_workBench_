let counter =1;
function changeText(){
    document.querySelector('p').innerHTML =
        "The button was pressed! (" + counter + "x)";
    counter++;
}
