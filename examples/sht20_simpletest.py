# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_sht20 import sht20


i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
sht = sht20.SHT20(i2c)

while True:
    print("Temperature: {:.2f} C".format(sht.temperature))
    print("Humidity: {:.2f} %%".format(sht.humidity))
    print("")
    time.sleep(1)
