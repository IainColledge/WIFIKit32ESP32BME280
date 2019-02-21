#
# Read BME 280 on I2C bus and display
#

import utime, ssd1306
import bme280
from machine import I2C, Pin


def main():
    # Common I2C bus
    i2c = I2C(scl=Pin(15), sda=Pin(4))

    # BME variables
    bme = bme280.BME280(i2c=i2c)

    # Display variables
    oled = ssd1306.SSD1306_I2C(128, 64, i2c)

    # Initialise the display
    pin16 = Pin(16, Pin.OUT)
    pin16.value(1)

    while True:
        oled.fill(0)
        oled.text('Temp: ' + bme.temperature, 0, 0)
        oled.text('Pres: ' + bme.pressure, 0, 10)
        oled.text('Hum: ' + bme.humidity, 0, 20)
        oled.show()
        utime.sleep(5)

if __name__ == '__main__':
    main()