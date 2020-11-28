print('Hello World!')

import time
import board
from digitalio import DigitalInOut, Direction, Pull
import displayio 
import terminalio
from adafruit_display_text import label
import adafruit_il0373
from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import label
import busio
import adafruit_bme680 
import adafruit_sgp30
from adafruit_display_shapes.rect import Rect
import adafruit_imageload

i2c = busio.I2C(board.SCL, board.SDA)
bme680_sensor = adafruit_bme680.Adafruit_BME680_I2C(i2c)

print('Temperature: {} degrees C'.format(bme680_sensor.temperature))
print('Gas: {} ohms'.format(bme680_sensor.gas))
print('Humidity: {}%'.format(bme680_sensor.humidity))
print('Pressure: {}hPa'.format(bme680_sensor.pressure))

sgp30_sensor = adafruit_sgp30.Adafruit_SGP30(i2c)
print("eCO2 = %d ppm \t TVOC = %d ppb" % (sgp30_sensor.eCO2, sgp30_sensor.TVOC))

display = board.DISPLAY

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT
led.value = True

group = displayio.Group(max_size=20)
# background
rect1 = Rect(0, 0, 208, 82, fill=0xFFFFFF)
rect2 = Rect(210, 0, 296, 82, fill=0xBBBBBB)
rect3 = Rect(0, 84, 296, 128, fill=0x444444)

# Create fonts
big_font = bitmap_font.load_font("/ExoBold-72.bdf")
medium_font = bitmap_font.load_font("/ExoSemiBold-36.bdf")
small_font = bitmap_font.load_font("/ExoSemiBold-24.bdf")

# Create sensor value labels
temperature_label = label.Label(big_font, text="012.45°", color=0x000000, x=28, y=40, background_color=0xFFFFFF)
humidity_label = label.Label(medium_font, text="12.34%", color=0xFFFFFF, x=12, y=106, background_color=0x444444)
pressure_label = label.Label(medium_font, text="1234hPa", color=0xFFFFFF, x=140, y=10, background_color=0x444444)
eco2_label = label.Label(small_font, text="1234ppm", color=0x000000, x=218, y=20, background_color=0xBBBBBB)
tvoc_label = label.Label(small_font, text="1234ppb", color=0x000000, x=218, y=50, background_color=0xBBBBBB)

## Bitmaps
thermometer_bitmap = displayio.OnDiskBitmap(open("/thermometer.bmp", "rb"))
tilegrid = displayio.TileGrid(thermometer_bitmap, pixel_shader=displayio.ColorConverter(), x=4, y=10)

# Compose group
group.append(rect1)
group.append(rect2)
group.append(rect3)
group.append(temperature_label)
group.append(humidity_label)
group.append(pressure_label)
group.append(eco2_label)
group.append(tvoc_label)
group.append(tilegrid)

remaining_time = 0

while True:
    time.sleep(1)
    remaining_time -= 1
    if remaining_time <= 0:
        remaining_time = 5 * 60

        print("========================")
        print('BME Temperature: {} C'.format(bme680_sensor.temperature))
        print('BME Gas: {} ohms'.format(bme680_sensor.gas))
        print('BME Humidity: {}%'.format(bme680_sensor.humidity))
        print('BME Pressure: {}hPa'.format(bme680_sensor.pressure))

        print("SGP eCO2 = %d ppm" % (sgp30_sensor.eCO2))
        print("SGP TVOC = %d ppb" % (sgp30_sensor.TVOC))

        temperature_label.text = "{:4.1f}°".format(bme680_sensor.temperature)
        humidity_label.text = "{:4.1f}%".format(bme680_sensor.humidity)
        pressure_label.text = "{:4.0f}hPa".format(bme680_sensor.pressure)
        eco2_label.text = "{:4.0f}ppm".format(sgp30_sensor.eCO2)
        tvoc_label.text = "{:4.0f}ppb".format(sgp30_sensor.TVOC)
        display.show(group)
        display.refresh()
