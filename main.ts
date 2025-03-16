input.onButtonPressed(Button.A, function () {
    pins.digitalWritePin(DigitalPin.P12, 1)
    pins.digitalWritePin(DigitalPin.P13, 0)
    basic.pause(2000)
    pins.digitalWritePin(DigitalPin.P12, 0)
    pins.digitalWritePin(DigitalPin.P13, 0)
})
input.onButtonPressed(Button.AB, function () {
    basic.showString(DS3231.dateString())
})
input.onButtonPressed(Button.B, function () {
    for (let index = 0; index < 4; index++) {
        pins.servoWritePin(AnalogPin.P9, 0)
        makerbit.showStringOnLcd1602("obrir", makerbit.position1602(LcdPosition1602.Pos1), 12)
        basic.pause(1000)
        pins.servoWritePin(AnalogPin.P9, 45)
        basic.pause(1000)
        pins.servoWritePin(AnalogPin.P9, 90)
        basic.pause(1000)
    }
})
let hum = 0
let temp = 0
pins.digitalWritePin(DigitalPin.P12, 0)
pins.digitalWritePin(DigitalPin.P13, 0)
let intruspir = 0
makerbit.connectLcd(39)
makerbit.showStringOnLcd1602("inici", makerbit.position1602(LcdPosition1602.Pos1), 6)
dht11_dht22.queryData(
DHTtype.DHT11,
DigitalPin.P16,
true,
false,
true
)
dht11_dht22.selectTempType(tempType.celsius)
DS3231.setDate(0, 5, 1, 2025)
basic.forever(function () {
    temp = dht11_dht22.readData(dataType.temperature)
    hum = dht11_dht22.readData(dataType.humidity)
    if (dht11_dht22.readDataSuccessful()) {
        makerbit.showStringOnLcd1602("T:", makerbit.position1602(LcdPosition1602.Pos1), 2)
        makerbit.showStringOnLcd1602("" + (temp), makerbit.position1602(LcdPosition1602.Pos3), 4)
        makerbit.showStringOnLcd1602("H:", makerbit.position1602(LcdPosition1602.Pos17), 2)
        makerbit.showStringOnLcd1602("" + (hum), makerbit.position1602(LcdPosition1602.Pos19), 4)
    } else {
    	
    }
    intruspir = pins.digitalReadPin(DigitalPin.P15)
    if (intruspir == 1) {
        makerbit.showStringOnLcd1602("Intrus!!", makerbit.position1602(LcdPosition1602.Pos8), 9)
    } else {
        makerbit.showStringOnLcd1602("", makerbit.position1602(LcdPosition1602.Pos8), 9)
    }
    basic.showString("" + (intruspir))
    basic.pause(1000)
    makerbit.showStringOnLcd1602("Gas", makerbit.position1602(LcdPosition1602.Pos24), 9)
    makerbit.showStringOnLcd1602("" + (pins.analogReadPin(AnalogReadWritePin.P10)), makerbit.position1602(LcdPosition1602.Pos27), 9)
})
