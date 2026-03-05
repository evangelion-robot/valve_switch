# RIGHTS RESERVED BY THE GOAT

from machine import Pin
import time 

# valve = 0 -> \/ and valve = 1 -> \\

valve = Pin(0, Pin.OUT)

while True:
    valve.value(1)
    time.sleep(1)
    valve.value(0)
    time.sleep(1)