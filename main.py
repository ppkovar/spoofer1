def on_button_pressed_a():
    global Attenuation
    Attenuation = Attenuation + 1
    if Attenuation == 32:
        Attenuation = 31
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Attenuation
    Attenuation = Attenuation - 1
    if Attenuation == -1:
        Attenuation = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

Att2 = 0
Att4 = 0
Att8 = 0
Att16 = 0
Attenuation = 0
Attenuation = 0
pins.digital_write_pin(DigitalPin.P5, 0)
pins.digital_write_pin(DigitalPin.P6, 0)
pins.digital_write_pin(DigitalPin.P7, 0)
pins.digital_write_pin(DigitalPin.P8, 0)
pins.digital_write_pin(DigitalPin.P9, 0)
pins.digital_write_pin(DigitalPin.P10, 0)

def on_forever():
    basic.show_number(Attenuation)
basic.forever(on_forever)

def on_forever2():
    global Att16, Att8, Att4, Att2
    Att16 = Attenuation / 16
    Att8 = Attenuation / 8
    Att4 = Attenuation / 4
    Att2 = Attenuation / 2
    pins.digital_write_pin(DigitalPin.P10, Attenuation % 2)
    pins.digital_write_pin(DigitalPin.P9, Att2 % 2)
    pins.digital_write_pin(DigitalPin.P8, Att4 % 2)
    pins.digital_write_pin(DigitalPin.P7, Att8 % 2)
    pins.digital_write_pin(DigitalPin.P6, Att16 % 2)
    basic.pause(1000)
    pins.digital_write_pin(DigitalPin.P5, 1)
    basic.pause(100)
    pins.digital_write_pin(DigitalPin.P5, 0)
basic.forever(on_forever2)
