#!/usr/bin/python3
'''
A GUI drawing app
'''
from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
from tkinter import messagebox


class PaintApp:
    '''
    A drawing GUI application
    '''

    def __init__(self, master):
        self.frame = ttk.Frame(master)

        self.style = ttk.Style()
        self.style.configure('TButton', font=('arial', 12))

        self.color = StringVar()
        self.color.set('#000000')
        self.prev = None

        self.canvas = Canvas(self.frame, width=250, height=250,
                             bd=2, highlightbackground='black', bg='white')
        self.canvas.grid(row=0, column=0, rowspan=5, padx=5, pady=5)
        self.canvas.create_rectangle(0, 0, self.canvas.winfo_width(
        ), self.canvas.winfo_height(), fill='#ffffff')
        self.canvas.bind('<1>', self.get_mouse_pos)
        self.canvas.bind('<B1-Motion>', self.draw_line)

        ttk.Button(self.frame, text="Select Color",
                   command=self.choose_color).grid(row=0, column=1, padx=5,
                                                   pady=5)

        ttk.Button(self.frame, text="Clear Canvas",
                   command=self.clear_canvas).grid(row=1, column=1, padx=5,
                                                   pady=5)

        self.frame.pack()

    def choose_color(self):
        '''
        Asks the user to pick a color to draw with
        and assigns the hex value of the chosen color
        to the color property of the object
        '''
        new_color = colorchooser.askcolor()[1]
        # Ensures that user selected a new color
        if new_color is not None:
            self.color.set(new_color)

    def get_mouse_pos(self, event):
        '''
        Gets the current mouse position and assigns
        it to the value of prev
        '''
        self.prev = event

    def draw_line(self, event):
        '''
        Draws a line that follows the user's cursor
        '''
        self.canvas.create_line(self.prev.x, self.prev.y,
                                event.x, event.y, width=5, fill=self.color.get())
        self.prev = event

    def clear_canvas(self):
        '''
        Clears the canvas
        '''
        self.canvas.delete('all')


def main():
    '''
    Executes script
    '''
    root = Tk()
    root.title("Draw Demo")
    PaintApp(root)

    root.mainloop()


if __name__ == "__main__":
    main()
