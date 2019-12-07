# clock
Raspberry Pi powered desk clock - integrating a 7 segment display, speaker, and LED ring.


## Wiring
**7-segment**
V_IO => 3.3V
VCC => 5V
GND => GND
SDA => SDA
SCL => SCL

**Speaker**
idk



## Setup
Attempting to revive my old clock project...
Found this link: https://github.com/adafruit/Adafruit_Python_LED_Backpack
This seems to be the updated libraries for the LED display

https://learn.adafruit.com/matrix-7-segment-led-backpack-with-the-raspberry-pi/overview



```
sudo raspi-config
# remember to enable i2c!!!
sudo apt-get install i2c-tools build-essential python-dev python-smbus python-imaging
```

*from a blank state raspberry pi...*
```
sudo apt-get install python3-pip
pip3 install adafruit-blinka
pip3 install adafruit-circuitpython-ht16k33
```


```
# This appears to be an older library that doesn't seem to work. The only thing that worked here was dimming the display.
git clone https://github.com/adafruit/Adafruit_Python_LED_Backpack.git
cd Adafruit_Python_LED_Backpack
sudo python3 setup.py install # because 'python' is still 2.7 on the pi...

```