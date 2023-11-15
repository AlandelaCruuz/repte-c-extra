radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    
    numcpu = randint(1, 6)
    basic.showNumber(numcpu)
    if (receivedNumber < numcpu) {
        basic.showIcon(IconNames.Happy)
    } else {
        basic.showIcon(IconNames.Sad)
    }
    
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    mynum = randint(1, 6)
    radio.sendNumber(mynum)
    basic.showNumber(mynum)
})
let mynum = 0
let numcpu = 0
