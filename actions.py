from gpiozero import LED
from time import sleep

led = LED(17)

def led_on():
    led.on()
def led_off():
    led.off()