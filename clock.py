# https://github.com/adafruit/Adafruit_CircuitPython_HT16K33/blob/master/adafruit_ht16k33/segments.py
import time
import board
import busio
import pytz
from adafruit_ht16k33 import segments
from datetime import datetime
i2c = busio.I2C(board.SCL, board.SDA)


def set_left_colon(display, value):
    set_top_left_dot(display, value)
    set_bottom_left_dot(display, value)

def set_top_left_dot(display, value):
    current = display._get_buffer(0x04)
    if value:
        display._set_buffer(0x04, current | 0x04) # top left
    else:
        display._set_buffer(0x04, current & ~0x04)
    display.show()

def set_bottom_left_dot(display, value):
    current = display._get_buffer(0x04)
    if value:
        display._set_buffer(0x04, current | 0x08) # bottom left
    else:
        display._set_buffer(0x04, current & ~0x08)
    display.show()



def main():
    print("Clock started...")

    display = segments.BigSeg7x4(i2c)
    display.fill(0)
    
    while True:
        now = datetime.now(tz=pytz.timezone('America/New_York'))
        hours = now.strftime('%-I').rjust(2)
        minutes = now.strftime('%M')
        display.print(hours + ':' + minutes)
        set_top_left_dot(display, now.strftime('%p') == 'AM')
        set_bottom_left_dot(display, now.strftime('%p') == 'PM')
        time.sleep(60 - time.time() % 60)


if __name__ == '__main__':
    main()

