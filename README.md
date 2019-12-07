# clock
Raspberry Pi powered desk clock - integrating a 7 segment display, speaker, and LED ring.

## Setup
Attempting to revive my old clock project...
Found this link: https://github.com/adafruit/Adafruit_Python_LED_Backpack
This seems to be the updated libraries for the LED display


*from a blank state raspberry pi...*
```
sudo apt-get install python3-pip
```


```
sudo apt-get install build-essential python-dev
sudo apt-get install python-smbus python-imaging
git clone https://github.com/adafruit/Adafruit_Python_LED_Backpack.git
cd Adafruit_Python_LED_Backpack
sudo python3 setup.py install # because 'python' is still 2.7 on the pi...

```