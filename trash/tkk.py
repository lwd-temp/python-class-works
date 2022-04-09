import pathlib
import pygubu
import tkinter as tk
import tkinter.ttk as ttk

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "新项目"


class 新项目App:
    def __init__(self, master=None):
        # build ui
        self.labelframe1 = tk.LabelFrame(master)
        self.entry1 = tk.Entry(self.labelframe1)
        self.entry1.pack(side='top')
        self.button1 = tk.Button(self.labelframe1)
        self.button1.configure(text='button1')
        self.button1.pack(side='top')
        self.labelframe1.configure(
            height='200', text='labelframe1', width='200')
        self.labelframe1.pack(side='top')

        # Main widget
        self.mainwindow = self.labelframe1

    def run(self):
        # Detect button click
        self.button1.bind('<Button-1>', self.button1_click)
        self.mainwindow.mainloop()

    # Click the button
    def button1_click(self, event):
        print('button1 clicked')


if __name__ == '__main__':
    root = tk.Tk()
    app = 新项目App(root)
    app.run()
