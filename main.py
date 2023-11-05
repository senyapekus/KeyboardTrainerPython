"""main file"""
import random
import unicodedata
from datetime import datetime
from tkinter import *
from tkinter import messagebox

import my_timer

CHECK = ''
TXT_SPEED = ''
TXT_TRAINER = 'йцукенгшщзхъфывапролджэячсмитьбюё123456789' \
              'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ'
start = datetime
TIMER_COMPLEXITY = False
LETTER_COUNTER = 0
t = my_timer.MyTimer(TIMER_COMPLEXITY)

with open("text_speed_test.txt", "r", encoding='utf8') as file:
    text_file = file.read().split('\n')


def clicked_exit():
    """exit"""
    window.destroy()


def start_over():
    """start over"""
    global TIMER_COMPLEXITY, LETTER_COUNTER
    LETTER_COUNTER = 0
    t.timer_reset(timer, LETTER_COUNTER)
    t.timer_start_pause(timer, messagebox, TIMER_COMPLEXITY)


def trainer_keypress(event):
    """trainer"""
    global LETTER_COUNTER
    if event.char == key['text']:
        LETTER_COUNTER += 1
        t.timer_reset(timer, LETTER_COUNTER)
        key['text'] = random.choice(TXT_TRAINER)


def hard_trainer():
    """hard trainer"""
    global TIMER_COMPLEXITY
    exit_btn.destroy()
    new_space.destroy()
    new_exit_btn.destroy()
    greeting.destroy()
    button1.destroy()
    button2.destroy()
    window.geometry('1100x600')

    TIMER_COMPLEXITY = True
    over_button = Button(window,
                         text="Начать заново",
                         font=('Arial Bold', 15),
                         command=start_over)
    exit_b = Button(window,
                    text='Выход',
                    font=('Arial Bold', 15),
                    anchor=CENTER,
                    command=clicked_exit)
    space_timer = Label(window,
                        text='\n\n')
    second_space_timer = Label(window,
                               text='\n\n')
    key.pack()
    space_timer.pack()
    timer.pack()
    second_space_timer.pack()
    over_button.pack()
    exit_b.pack()

    t.timer_start_pause(timer, messagebox, True)

    window.bind("<Key>", trainer_keypress)


def normal_trainer():
    """normal trainer"""
    exit_btn.destroy()
    new_space.destroy()
    new_exit_btn.destroy()
    greeting.destroy()
    button1.destroy()
    button2.destroy()
    window.geometry('1100x600')

    over_button = Button(window,
                         text="Начать заново",
                         font=('Arial Bold', 15),
                         command=start_over)
    exit_b = Button(window,
                    text='Выход',
                    font=('Arial Bold', 15),
                    anchor=CENTER,
                    command=clicked_exit)
    space_timer = Label(window,
                        text='\n\n')
    second_space_timer = Label(window,
                               text='\n\n')
    key.pack()
    space_timer.pack()
    timer.pack()
    second_space_timer.pack()
    over_button.pack()
    exit_b.pack()

    t.timer_start_pause(timer, messagebox, False)

    window.bind("<Key>", trainer_keypress)


def handle_keypress(event):
    """handle keypress"""
    global check
    global v
    global start

    if event.char == txt_speed[0]:
        start = datetime.now()
    if event.char == '.':
        time = float(str(datetime.now() - start).split(':')[2])
        result = int((60 * len(txt_speed)) / time)
        check = unicodedata.normalize('NFC', v.get())
        if check == txt_speed:
            messagebox.showinfo('Результат', 'Вы печатаете примерно '
                                             '{} сим/минуту'.format(result))
        else:
            messagebox.showwarning('Результат', 'Похоже, вы допустили ошибку'
                                                '\nПопробуйте снова.')


def clicked_trainer():
    """clicked trainer"""
    exit_btn.destroy()
    first_space.destroy()
    second_space.destroy()
    greeting['text'] = 'В данном режиме вам нужно нажать' \
                       '\nна появившуюся клавишу, пока не истек\nтаймер' \
                       '\n\nВыберите уровень сложности\n(русская раскладка):'
    greeting['font'] = ('Arial Bold', 18)
    button1['text'] = 'Нормальный'
    button2['text'] = 'Сложный'
    button1['command'] = normal_trainer
    button2['command'] = hard_trainer

    new_space.pack()
    new_exit_btn.pack()


def clicked_speed():
    """speed"""
    global txt_speed
    exit_btn.destroy()
    greeting.destroy()
    first_space.destroy()
    second_space.destroy()
    button1.destroy()
    button2.destroy()
    window.geometry('1350x600')
    txt_speed = unicodedata.normalize('NFC', random.choice(text_file))
    greeting_speed = Label(window,
                           text='Как будешь готов,'
                                ' начинай печатать текст в рамке:',
                           font=('Arial Bold', 20),
                           anchor=CENTER)
    txt = Label(window, text=txt_speed,
                font=('Arial Bold', 18),
                anchor=CENTER,
                height=3,
                relief=RIDGE,
                pady=5)
    entry = Entry(window,
                  width=100,
                  textvariable=v)

    greeting_speed.pack()
    txt.pack()
    entry.pack()
    new_space.pack()
    new_exit_btn.pack()

    window.bind("<Key>", handle_keypress)


if __name__ == '__main__':
    window = Tk()
    window.geometry('560x400')
    window.title('Клавиатурный тренажер')
    greeting = Label(window,
                     text='Приветствуем в Клавиатурном тренажере!',
                     font=('Arial Bold', 20),
                     anchor=CENTER)
    first_space = Label(window,
                        text='\n\n')
    second_space = Label(window,
                         text='\n\n')
    new_space = Label(window,
                      text='\n\n\n')
    button1 = Button(window,
                     text="Узнать свою скорость печати",
                     font=('Arial Bold', 15),
                     command=clicked_speed)
    button2 = Button(window,
                     text="Улучшить навыки печати",
                     font=('Arial Bold', 15),
                     command=clicked_trainer)
    exit_btn = Button(window,
                      text='Выход',
                      font=('Arial Bold', 15),
                      anchor=CENTER,
                      command=clicked_exit)
    new_exit_btn = Button(window,
                          text='Выход',
                          font=('Arial Bold', 15),
                          anchor=CENTER,
                          command=clicked_exit)
    timer = Label(window,
                  font=('Arial Bold', 25),
                  fg='#006400',
                  relief=SUNKEN,
                  height=2,
                  width=3)
    key = Label(window,
                text=random.choice(TXT_TRAINER),
                font=('Arial Bold', 25),
                anchor=CENTER,
                height=2,
                width=1,
                relief=RAISED,
                padx=55,
                pady=5,
                bd=10,
                bg='#FFFFE0')

    v = StringVar()
    greeting.pack()
    first_space.pack()
    button1.pack()
    button2.pack()
    second_space.pack()
    exit_btn.pack()

    window.mainloop()
