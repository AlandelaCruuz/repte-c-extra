def on_received_number(receivedNumber):
    global numcpu
    numcpu = randint(1, 6)
    basic.show_number(numcpu)
    if receivedNumber < numcpu:
        basic.show_icon(IconNames.HAPPY)
    else:
        basic.show_icon(IconNames.SAD)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global mynum
    mynum = randint(1, 6)
    radio.send_number(mynum)
    basic.show_number(mynum)
input.on_button_pressed(Button.A, on_button_pressed_a)

mynum = 0
numcpu = 0
