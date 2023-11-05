"""app file"""
import tkinter as tk

from controller import Controller
from model import Model
from view import View


class App(tk.Tk):
    """create app"""
    def __init__(self):
        super().__init__()

        model = Model('text_speed_test.txt')

        view = View(self)

        controller = Controller(model, view)

        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()
