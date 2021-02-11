from microbit import *

seconds = 0
display_num = 0
count = 0

if button_a.is_pressed():
    count = 1
    display_num = 1

if button_b.is_pressed():
    if count == 1 and display_num == 1:
        count = 0
    elif count == 0 and display_num == 1:
        display_num = 0
        seconds = 0
        display.clear()

while True:
    if display_num == 1:
        basic.show_number(seconds)
    if count == 1:
        seconds += 1
        sleep(1000)
