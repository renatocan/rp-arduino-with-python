import pyfirmata
import time

board = pyfirmata.Arduino('/dev/ttyACM0')

it = pyfirmata.util.Iterator(board)
it.start()

digital_input = board.get_pin('d:10:i')
led = board.get_pin('d:13:o')

while True:
    if digital_input.value is True:
        led.write(1)
    else:
        led.write(0)
    time.sleep(0.1)
