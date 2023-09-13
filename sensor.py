from gpiozero import LED
from gpiozero import GPIODevice
from gpiozero import InputDevice
inputd=InputDevice(17)
value=inputd.value
print(value)