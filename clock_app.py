#!/usr/bin/python3
'''
A simple GUI clock
'''
from tkinter import *
from tkinter import ttk

from datetime import datetime


class ClockApp():
    '''
    A simple clock GUI application
    '''

    def __init__(self, master):

        self.frame = ttk.Frame(master, relief=RIDGE, padding=(15, 15))
        self.frame.pack()

        self._time_string = StringVar(
            value=datetime.today().strftime("Current time: %I:%M:%S %p"))

        self.label = ttk.Label(self.frame, text="Clock", justify=LEFT)
        self.label.config(font=("Courier", 18))
        self.label.pack()

        self.clock = ttk.Label(self.frame, textvariable=self._time_string)
        self.clock.pack()

        # Starts time update loop
        self._update_time()

    def _update_time(self):
        '''
        Updates the current time string in _time_string
        every second
        '''
        self._time_string.set(value=datetime.today(
        ).strftime("Current time: %I:%M:%S %p"))

        self.frame.after(1000, self._update_time)


def main():
    '''
    Demonstration
    '''

    root = Tk()
    root.title("Clock Demo")
    # my_clock = ClockApp(root)
    ClockApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
