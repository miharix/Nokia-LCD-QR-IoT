import board
import digitalio
import busio
import adafruit_pcd8544
import os
from PIL import Image

#definiraj GPIO
spi = busio.SPI(board.SCK, MOSI=board.MOSI)
dc = digitalio.DigitalInOut(board.D6)
cs = digitalio.DigitalInOut(board.CE0)
reset = digitalio.DigitalInOut(board.D5)

display = adafruit_pcd8544.PCD8544(spi, dc, cs, reset)

# Konstrast in svetlost
display.contrast = 60
display.bias = 4

# Za vklop luci ozadja
backlight = digitalio.DigitalInOut(board.D13)
backlight.switch_to_output()
backlight.value = False #Zamenjaj False z True za vklop luci ozadja

#prenesi sliko iz streznika
url = 'https://tim.izdelal.si/koledar/index.php'
ukaz = 'wget '+url+" -O prikaz.bmp"
os.system(ukaz)

#nalozi sliko - 84x48px 1 bit bmp 
slika=Image.open("prikaz.bmp")

#prikazi sliko
display.image(slika)
display.show()

