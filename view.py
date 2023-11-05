"""view in mvc-pattern"""
import random
from tkinter import *
from tkinter import ttk


class View(ttk.Frame):
    """view"""
    def __init__(self, parent):
        super().__init__(parent)

        self.window = parent
        self.window.geometry('560x400')
        self.window.title('Клавиатурный тренажер')
        self.greeting = Label(self.window,
                              text='Приветствуем в Клавиатурном тренажере!',
                              font=('Arial Bold', 20),
                              anchor=CENTER)
        self.first_space = Label(self.window,
                                 text='\n\n')
        self.second_space = Label(self.window,
                                  text='\n\n')
        self.new_space = Label(self.window,
                               text='\n\n\n')
        self.button1 = Button(self.window,
                              text="Узнать свою скорость печати",
                              font=('Arial Bold', 15))
        self.button2 = Button(self.window,
                              text="Улучшить навыки печати",
                              font=('Arial Bold', 15))
        self.exit_btn = Button(self.window,
                               text='Выход',
                               font=('Arial Bold', 15),
                               anchor=CENTER)
        self.new_exit_btn = Button(self.window,
                                   text='Выход',
                                   font=('Arial Bold', 15),
                                   anchor=CENTER)
        self.timer = Label(self.window,
                           font=('Arial Bold', 25),
                           fg='#006400',
                           relief=SUNKEN,
                           height=2,
                           width=3)
        self.key = Label(self.window,
                         font=('Arial Bold', 25),
                         anchor=CENTER,
                         height=2,
                         width=1,
                         relief=RAISED,
                         padx=55,
                         pady=5,
                         bd=10,
                         bg='#FFFFE0')
        self.over_button = Button(self.window,
                                  text="Начать заново",
                                  font=('Arial Bold', 15))
        self.exit_b = Button(self.window,
                             text='Выход',
                             font=('Arial Bold', 15),
                             anchor=CENTER)
        self.space_timer = Label(self.window,
                                 text='\n\n')
        self.second_space_timer = Label(self.window,
                                        text='\n\n')

        self.v = StringVar()
        self.greeting.pack()
        self.first_space.pack()
        self.button1.pack()
        self.button2.pack()
        self.second_space.pack()
        self.exit_btn.pack()

        self.controller = None

    def set_controller(self, controller):
        """set controller"""
        print('set_c start')
        self.controller = controller

        self.button1.configure(command=self.controller.clicked_speed)
        self.button2.configure(command=self.controller.clicked_trainer)
        self.exit_btn.configure(command=self.controller.clicked_exit)
        self.new_exit_btn.configure(command=self.controller.clicked_exit)
        self.over_button.configure(command=self.controller.start_over)
        self.exit_b.configure(command=self.controller.clicked_exit)
        self.key['text'] = random.choice(self.controller.txt_trainer)
