# main.py -- put your code here!
from pyb import UART
while True:
    uart = UART(1, 9600)
    x = uart.read()
    print(str(x))
