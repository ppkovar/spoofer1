input.onButtonPressed(Button.A, function () {
    Attenuation = Attenuation + 1
    if (Attenuation == 32) {
        Attenuation = 31
    }
})
input.onButtonPressed(Button.B, function () {
    Attenuation = Attenuation - 1
    if (Attenuation == -1) {
        Attenuation = 0
    }
})
let Att2 = 0
let Att4 = 0
let Att8 = 0
let Att16 = 0
let Attenuation = 0
Attenuation = 0
pins.digitalWritePin(DigitalPin.P0, 0)
pins.digitalWritePin(DigitalPin.P1, 0)
pins.digitalWritePin(DigitalPin.P2, 0)
pins.digitalWritePin(DigitalPin.P8, 0)
pins.digitalWritePin(DigitalPin.P9, 0)
pins.digitalWritePin(DigitalPin.P12, 0)
basic.forever(function () {
    basic.showNumber(Attenuation)
})
basic.forever(function () {
    Att16 = Math.floor(Attenuation / 16)
    Att8 = Math.floor(Attenuation / 8)
    Att4 = Math.floor(Attenuation / 4)
    Att2 = Math.floor(Attenuation / 2)
    pins.digitalWritePin(DigitalPin.P12, Attenuation % 2)
    pins.digitalWritePin(DigitalPin.P9, Att2 % 2)
    pins.digitalWritePin(DigitalPin.P8, Att4 % 2)
    pins.digitalWritePin(DigitalPin.P2, Att8 % 2)
    pins.digitalWritePin(DigitalPin.P1, Att16 % 2)
    basic.pause(1000)
    pins.digitalWritePin(DigitalPin.P0, 1)
    basic.pause(100)
    pins.digitalWritePin(DigitalPin.P0, 0)
})
