let seconds = 0;
let display = false;
let count = false;

input.onButtonPressed(Button.A, function () {
    count = true;
    display = true;
})

input.onButtonPressed(Button.B, function () {
    if (count === true && display === true)
        count = false;
    else if (count === false && display === true){
        display = false;
        seconds = 0;
        basic.clearScreen();
    }
})

basic.forever(function () {
    if (display){
        basic.showNumber(seconds);
    }
    if (count){
        seconds = seconds + 1;
        basic.pause(100);
    }
})
