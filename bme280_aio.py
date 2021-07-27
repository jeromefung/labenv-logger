'''
Log temperature and humidity from Adafruit BME 280
and send to Adafruit IO.
'''

import board
from adafruit_bme280 import basic as adafruit_bme280
from Adafruit_IO import Client, Feed
import time
import json

# Set up I2C communication to sensor
i2c = board.I2C()
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

# Load login info from file
with open('/home/pi/funglab_logger/aio_login.json') as f:
    aio_dict = json.load(f)

# Set up connection to Adafruit IO
aio = Client(aio_dict['aio_username'], aio_dict['aio_key'])

while True:
    aio.send('funglab-temperature', bme280.temperature)
    aio.send('funglab-humidity', bme280.humidity)
    time.sleep(30)


