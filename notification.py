import pyfirmata
import time
import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.withdraw()

board = pyfirmata.Arduino('/dev/ttyACM0')

it = pyfirmata.util.Iterator(board)
it.start()

digital_input = board.get_pin('d:10:i')
led = board.get_pin('d:13:o')

while True:
    sw = digital_input.read()
    if sw is True:
        led.write(1)
        messagebox.showinfo("Title", "a Tk MessageBox")
        root.update()
        led.write(0)
        time.sleep(0.1)
