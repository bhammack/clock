# clock
Raspberry Pi powered desk clock - integrating a 7 segment display, speaker, and LED ring.

## Housing
*Similar projects*
* https://github.com/alexjohnmartin/RetroPieArcadeCabinet
* https://clock.bonsignore.com/
Looks like I want to use 3mm plywood

**Current Clock Dimensions**
6" Wide
2.5" Tall
5.5" Deep
** Raspberry Pi Mounting **
* https://www.raspberrypi.org/documentation/hardware/raspberrypi/mechanical/rpi_MECH_3bplus.pdf
* https://www.raspberrypi.org/documentation/hardware/raspberrypi/mechanical/rpi_MECH_3bplus_case.pdf
* The pi uses M2.5 mounting holes, but can use M3 with some modification.


## Wiring
https://www.adafruit.com/product/1269
**7-segment -> Pi**
* V_IO => 3.3V
* VCC => 5V
* GND => GND
* SDA => SDA
* SCL => SCL

**Speaker -> Pi**
https://www.adafruit.com/product/3006
* Vin to Raspbery Pi 5V
* GND to Raspbery Pi GND
* DIN to Raspbery Pi #21
* BCLK to Raspbery Pi #18
* LRCLK to Raspbery Pi #19

## Setup
### 7-Segment Display
Attempting to revive my old clock project...
Found this link: https://github.com/adafruit/Adafruit_Python_LED_Backpack
This seems to be the updated libraries for the LED display

https://learn.adafruit.com/matrix-7-segment-led-backpack-with-the-raspberry-pi/overview


*from a blank state raspberry pi...*
```
sudo raspi-config
# remember to enable i2c!!!
sudo apt-get install i2c-tools build-essential python-dev python-smbus python3-pip git tmux
# you can run i2cdetect to verify an address is listed on the i2c bus
pip3 install adafruit-blinka adafruit-circuitpython-ht16k33 pytz
git clone https://github.com/bhammack/clock.git
```

```
# This appears to be an older library that doesn't seem to work. The only thing that worked here was dimming the display.
git clone https://github.com/adafruit/Adafruit_Python_LED_Backpack.git
cd Adafruit_Python_LED_Backpack
sudo python3 setup.py install # because 'python' is still 2.7 on the pi...

```

### Speaker
Super easy to set up. Run the script below and it will autoconfigure the i2s drivers!
https://learn.adafruit.com/adafruit-max98357-i2s-class-d-mono-amp/raspberry-pi-wiring
```
curl -sS https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/i2samp.sh | bash
sudo apt-get install -y mpg123
mpg123 http://ice1.somafm.com/u80s-128-mp3
```