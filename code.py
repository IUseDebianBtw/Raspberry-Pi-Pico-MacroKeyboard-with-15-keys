import time
import board
import digitalio
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode


cc = ConsumerControl(usb_hid.devices)


keyboard = Keyboard(usb_hid.devices)


write_text = KeyboardLayoutUS(keyboard)



btn1_pin = board.GP0
btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2_pin = board.GP1
btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3_pin = board.GP2
btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

btn4_pin = board.GP3
btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN

btn5_pin = board.GP4
btn5 = digitalio.DigitalInOut(btn5_pin)
btn5.direction = digitalio.Direction.INPUT
btn5.pull = digitalio.Pull.DOWN

btn6_pin = board.GP5
btn6 = digitalio.DigitalInOut(btn6_pin)
btn6.direction = digitalio.Direction.INPUT
btn6.pull = digitalio.Pull.DOWN

btn7_pin = board.GP6
btn7 = digitalio.DigitalInOut(btn7_pin)
btn7.direction = digitalio.Direction.INPUT
btn7.pull = digitalio.Pull.DOWN

#this is the second board

btn8_pin = board.GP7
btn8 = digitalio.DigitalInOut(btn8_pin)
btn8.direction = digitalio.Direction.INPUT
btn8.pull = digitalio.Pull.DOWN

btn9_pin = board.GP8
btn9 = digitalio.DigitalInOut(btn9_pin)
btn9.direction = digitalio.Direction.INPUT
btn9.pull = digitalio.Pull.DOWN

btn10_pin = board.GP9
btn10 = digitalio.DigitalInOut(btn10_pin)
btn10.direction = digitalio.Direction.INPUT
btn10.pull = digitalio.Pull.DOWN

btn11_pin = board.GP10
btn11 = digitalio.DigitalInOut(btn11_pin)
btn11.direction = digitalio.Direction.INPUT
btn11.pull = digitalio.Pull.DOWN

btn12_pin = board.GP11
btn12 = digitalio.DigitalInOut(btn12_pin)
btn12.direction = digitalio.Direction.INPUT
btn12.pull = digitalio.Pull.DOWN

btn13_pin = board.GP12
btn13 = digitalio.DigitalInOut(btn13_pin)
btn13.direction = digitalio.Direction.INPUT
btn13.pull = digitalio.Pull.DOWN

btn14_pin = board.GP13
btn14 = digitalio.DigitalInOut(btn14_pin)
btn14.direction = digitalio.Direction.INPUT
btn14.pull = digitalio.Pull.DOWN

btn15_pin = board.GP14
btn15 = digitalio.DigitalInOut(btn15_pin)
btn15.direction = digitalio.Direction.INPUT
btn15.pull = digitalio.Pull.DOWN





while True:
    
    #btn1
    # Keycode class defines USB HID keycodes to send using Keyboard.  
    if btn1.value:
        keyboard.send(Keycode.GUI)
        time.sleep(0.4)
        write_text.write('Brave\n')
        time.sleep(0.4)
    #btn2   
    if btn2.value:
        keyboard.send(Keycode.CONTROL, Keycode.T)
        time.sleep(0.4)
        write_text.write('put text here\n')
        time.sleep(0.4)

    #btn3 
    if btn3.value:
        keyboard.send(Keycode.CONTROL, Keycode.T)
        time.sleep(0.4)
        write_text.write('youtube.com\n')
        time.sleep(0.4)
    #btn4
    if btn4.value:
        write_text.write('put text here')
        time.sleep(0.4)
    #btn5
    if btn5.value:
        cc.send(ConsumerControlCode.PLAY_PAUSE)
        time.sleep(0.5)
    #btn6
    if btn6.value:
        cc.send(ConsumerControlCode.VOLUME_DECREMENT)
        time.sleep(0.1)
        
    #btn7
    if btn7.value:
        cc.send(ConsumerControlCode.VOLUME_INCREMENT)
        time.sleep(0.1)
        
    #btn8 
    if btn8.value:
        keyboard.send(Keycode.CONTROL, Keycode.F)
        time.sleep(0.1)
        
    #btn9
    if btn9.value:
        keyboard.send(Keycode.CONTROL, Keycode.A)
        time.sleep(0.1)
    #btn10
    if btn10.value:
        keyboard.send(Keycode.GUI)
        time.sleep(0.4)
        write_text.write('Terminal\n')
        time.sleep(0.4)
    #btn11
    if btn11.value:
        keyboard.send(Keycode.CONTROL, Keycode.T)
        time.sleep(0.4)
        write_text.write('https://discord.com/\n')
        time.sleep(0.4)
    #btn12
    if btn12.value:
        keyboard.send(Keycode.GUI)
        time.sleep(0.4)
        write_text.write('Discord\n')
        time.sleep(0.4)
    #btn13
    if btn13.value:
        keyboard.send(Keycode.GUI)
        time.sleep(0.4)
        write_text.write('VSCode\n')
        time.sleep(0.4)
    #btn14
    if btn14.value:
        keyboard.send(Keycode.GUI)
        time.sleep(0.4)
        write_text.write('Thonny\n')
        time.sleep(0.4)
    #btn15 make startup here
    if btn15.value:
        keyboard.send(Keycode.GUI)
        time.sleep(0.4)
        write_text.write('Brave\n')
        time.sleep(0.4)
        write_text.write('discord.com')
        time.sleep(0.4)
        keyboard.send(Keycode.CONTROL, Keycode.T)
        time.sleep(0.4)
        write_text.write('youtube.com\n')
        time.sleep(0.4)
        keyboard.send(Keycode.CONTROL, Keycode.T)
        time.sleep(0.4)
        write_text.write('google.comn')
        time.sleep(0.4)

    
