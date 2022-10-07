import random
from tkinter import *
from tkinter import messagebox
from datetime import datetime
import my_timer

check = ''
txt_speed = 'Набери этот текст без ошибок и узнай свою скорость печати.'
txt_trainer = 'йцукенгшщзхъфывапролджэячсмитьбю123456789'
start = datetime
timer_complexity = False
t = my_timer.MyTimer(timer_complexity)


def clicked_exit():
    window.destroy()


def start_over():
    global timer_complexity
    t.timer_reset(timer)
    t.timer_start_pause(timer, messagebox, timer_complexity)


def trainer_keypress(event):
    if event.char == key['text']:
        t.timer_reset(timer)
        key['text'] = random.choice(txt_trainer)


def hard_trainer():
    global timer_complexity
    exit_btn.destroy()
    new_space.destroy()
    new_exit_btn.destroy()
    greeting.destroy()
    button1.destroy()
    button2.destroy()
    window.geometry('1100x600')

    timer_complexity = True
    over_button = Button(window,
                         text="Начать заново",
                         font=('Arial Bold', 15),
                         command=start_over)
    exit = Button(window,
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
    exit.pack()

    t.timer_start_pause(timer, messagebox, True)

    window.bind("<Key>", trainer_keypress)


def normal_trainer():
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
    exit = Button(window,
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
    exit.pack()

    t.timer_start_pause(timer, messagebox, False)

    window.bind("<Key>", trainer_keypress)


def handle_keypress(event):
    global check
    global v
    global start

    if event.char == txt_speed[0]:
        start = datetime.now()
    if event.char == '.':
        time = float(str(datetime.now() - start).split(':')[2])
        result = int((60 * len(txt_speed)) / time)
        check = v.get()
        if check == txt_speed:
            messagebox.showinfo('Результат', 'Вы печатаете примерно '
                                             '{} сим/минуту'.format(result))
        else:
            messagebox.showwarning('Результат', 'Похоже, вы допустили ошибку'
                                                '\nПопробуйте снова.')


def clicked_trainer():
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
    exit_btn.destroy()
    greeting.destroy()
    first_space.destroy()
    second_space.destroy()
    button1.destroy()
    button2.destroy()
    window.geometry('1100x600')
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
                text=random.choice(txt_trainer),
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
