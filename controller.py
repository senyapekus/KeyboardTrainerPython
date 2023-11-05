"""controller in mvc-pattern"""
import random
import unicodedata
from datetime import datetime
from tkinter import CENTER, RIDGE, Entry, Label, messagebox

import my_timer


class Controller:
    """create controller"""
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.check = ''
        self.txt_speed = ''
        self.txt_trainer = 'йцукенгшщзхъфывапролджэячсмитьбюё123456789' \
                           'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ'
        self.start = datetime
        self.timer_complexity = False
        self.letter_counter = 0
        self.t = my_timer.MyTimer(self.timer_complexity)

    def clicked_exit(self):
        """exit"""
        self.view.window.destroy()

    def clicked_speed(self):
        """speed"""
        self.view.exit_btn.destroy()
        self.view.greeting.destroy()
        self.view.first_space.destroy()
        self.view.second_space.destroy()
        self.view.button1.destroy()
        self.view.button2.destroy()
        self.view.window.geometry('1350x600')
        self.txt_speed = unicodedata.normalize('NFC', random.choice(self.model.text_file))
        greeting_speed = Label(self.view.window,
                               text='Как будешь готов,'
                                    ' начинай печатать текст в рамке:',
                               font=('Arial Bold', 20),
                               anchor=CENTER)
        txt = Label(self.view.window, text=self.txt_speed,
                    font=('Arial Bold', 18),
                    anchor=CENTER,
                    height=3,
                    relief=RIDGE,
                    pady=5)
        entry = Entry(self.view.window,
                      width=100,
                      textvariable=self.view.v)

        greeting_speed.pack()
        txt.pack()
        entry.pack()
        self.view.new_space.pack()
        self.view.new_exit_btn.pack()

        self.view.window.bind("<Key>", self.handle_keypress)

    def clicked_trainer(self):
        """trainer"""
        self.view.exit_btn.destroy()
        self.view.first_space.destroy()
        self.view.second_space.destroy()
        self.view.greeting['text'] = 'В данном режиме вам нужно нажать' \
                                     '\nна появившуюся клавишу, пока не истек\nтаймер' \
                                     '\n\nВыберите уровень сложности\n(русская раскладка):'
        self.view.greeting['font'] = ('Arial Bold', 18)
        self.view.button1['text'] = 'Нормальный'
        self.view.button2['text'] = 'Сложный'
        self.view.button1['command'] = self.normal_trainer
        self.view.button2['command'] = self.hard_trainer

        self.view.new_space.pack()
        self.view.new_exit_btn.pack()

    def handle_keypress(self, event):
        """keypress"""
        if event.char == self.txt_speed[0]:
            self.start = datetime.now()
        if event.char == '.':
            time = float(str(datetime.now() - self.start).split(':')[2])
            result = int((60 * len(self.txt_speed)) / time)
            self.check = unicodedata.normalize('NFC', self.view.v.get())
            if self.check == self.txt_speed:
                messagebox.showinfo('Результат', 'Вы печатаете примерно '
                                                 '{} сим/минуту'.format(result))
            else:
                messagebox.showwarning('Результат', 'Похоже, вы допустили ошибку'
                                                    '\nПопробуйте снова.')

    def start_over(self):
        """start over"""
        self.letter_counter = 0
        self.t.timer_reset(self.view.timer, self.letter_counter)
        self.t.timer_start_pause(self.view.timer, messagebox, self.timer_complexity)

    def hard_trainer(self):
        """hard trainer mode"""
        self.view.exit_btn.destroy()
        self.view.new_space.destroy()
        self.view.new_exit_btn.destroy()
        self.view.greeting.destroy()
        self.view.button1.destroy()
        self.view.button2.destroy()
        self.view.window.geometry('1100x600')

        self.timer_complexity = True

        self.view.key.pack()
        self.view.space_timer.pack()
        self.view.timer.pack()
        self.view.second_space_timer.pack()
        self.view.over_button.pack()
        self.view.exit_b.pack()

        self.t.timer_start_pause(self.view.timer, messagebox, True)

        self.view.window.bind("<Key>", self.trainer_keypress)

    def normal_trainer(self):
        """normal trainer mode"""
        self.view.exit_btn.destroy()
        self.view.new_space.destroy()
        self.view.new_exit_btn.destroy()
        self.view.greeting.destroy()
        self.view.button1.destroy()
        self.view.button2.destroy()
        self.view.window.geometry('1100x600')

        self.view.key.pack()
        self.view.space_timer.pack()
        self.view.timer.pack()
        self.view.second_space_timer.pack()
        self.view.over_button.pack()
        self.view.exit_b.pack()

        self.t.timer_start_pause(self.view.timer, messagebox, False)

        self.view.window.bind("<Key>", self.trainer_keypress)

    def trainer_keypress(self, event):
        """trainer keypress"""
        if event.char == self.view.key['text']:
            self.letter_counter += 1
            self.t.timer_reset(self.view.timer, self.letter_counter)
            self.view.key['text'] = random.choice(self.txt_trainer)
