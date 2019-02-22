# WIFI Kit 32 ESP32 BME280

Code written in [micropython](http://micropython.org/) for the [WIFI Kit 32 ESP32 WIFI wireless with 0.96 inch OLED Display dev board](https://www.amazon.co.uk/gp/product/B078MCR8FY/ref=ppx_yo_dt_b_asin_title_o03__o00_s00?ie=UTF8&psc=1) to hook up to the Adafruit [BME280](https://www.adafruit.com/product/2652) breakout board.

## Wiring

Wire up as follows:

Wifi Kit 32 | BME280
:---: | :---:
GND | GND
3V3 | Vin
15 | SCK
4 | SDI

A wired up example is shown below.

![Wired Bpard](https://raw.githubusercontent.com/IainColledge/WIFIKit32ESP32BME280/master/board.jpg)

### Notes

Requires the BME280 driver from the [uPython library](https://github.com/IainColledge/uPythonDevices).