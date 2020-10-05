from bluedot import BlueDot
from gpiozero import LED
from signal import pause

bd = BlueDot()
led = LED(27)

bd.when_pressed = led.off
bd.when_released = led.on

pause()
