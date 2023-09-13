from gpiozero import LED
from gpiozero import GPIODevice

inputd=InputDevice(17)
value=inputd.value
print(value)