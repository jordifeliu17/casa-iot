def on_button_pressed_a():
    pins.digital_write_pin(DigitalPin.P12, 1)
    pins.digital_write_pin(DigitalPin.P13, 0)
    basic.pause(2000)
    pins.digital_write_pin(DigitalPin.P12, 0)
    pins.digital_write_pin(DigitalPin.P13, 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_string(DS3231.date_string())
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    for index in range(4):
        pins.servo_write_pin(AnalogPin.P9, 0)
        makerbit.show_string_on_lcd1602("obrir", makerbit.position1602(LcdPosition1602.POS1), 12)
        basic.pause(1000)
        pins.servo_write_pin(AnalogPin.P9, 45)
        basic.pause(1000)
        pins.servo_write_pin(AnalogPin.P9, 90)
        basic.pause(1000)
input.on_button_pressed(Button.B, on_button_pressed_b)

hum = 0
temp = 0
pins.digital_write_pin(DigitalPin.P12, 0)
pins.digital_write_pin(DigitalPin.P13, 0)
intruspir = 0
makerbit.show_string_on_lcd1602("inici", makerbit.position1602(LcdPosition1602.POS1), 6)
dht11_dht22.query_data(DHTtype.DHT11, DigitalPin.P16, True, False, True)
dht11_dht22.select_temp_type(tempType.CELSIUS)
DS3231.set_date(0, 5, 1, 2025)

def on_forever():
    global temp, hum, intruspir
    temp = dht11_dht22.read_data(dataType.TEMPERATURE)
    hum = dht11_dht22.read_data(dataType.HUMIDITY)
    if dht11_dht22.read_data_successful():
        makerbit.show_string_on_lcd1602("T:", makerbit.position1602(LcdPosition1602.POS1), 2)
        makerbit.show_string_on_lcd1602("" + str((temp)),
            makerbit.position1602(LcdPosition1602.POS3),
            4)
        makerbit.show_string_on_lcd1602("H:", makerbit.position1602(LcdPosition1602.POS17), 2)
        makerbit.show_string_on_lcd1602("" + str((hum)),
            makerbit.position1602(LcdPosition1602.POS19),
            4)
    else:
        pass
    intruspir = pins.digital_read_pin(DigitalPin.P15)
    if intruspir == 1:
        makerbit.show_string_on_lcd1602("Intrus!!", makerbit.position1602(LcdPosition1602.POS8), 9)
    else:
        makerbit.show_string_on_lcd1602("", makerbit.position1602(LcdPosition1602.POS8), 9)
    basic.show_string("" + str((intruspir)))
    basic.pause(1000)
    makerbit.show_string_on_lcd1602("Gas", makerbit.position1602(LcdPosition1602.POS24), 9)
    makerbit.show_string_on_lcd1602("" + str((pins.analog_read_pin(AnalogReadWritePin.P10))),
        makerbit.position1602(LcdPosition1602.POS27),
        9)
basic.forever(on_forever)
