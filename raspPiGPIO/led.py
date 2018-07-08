from gpiozero import LED
from time import sleep

led = LED(17)

for i in range(100):
   led.on()
   sleep(0.3)
   led.off()
   sleep(0.5)
