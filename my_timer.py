"""timer realisation"""


class MyTimer:
    """timer"""
    def __init__(self, timer_complexity):
        self.timer_complexity = timer_complexity  # false - normal, true - hard
        self.timer_running = False
        self.default_seconds = 1 if self.timer_complexity else 3
        self.timer_seconds = self.default_seconds
        self.letter_counter = 0

    def timer_start_pause(self, timer, messagebox, timer_complexity):
        """start/pause"""
        self.timer_running = True
        if timer_complexity:
            self.default_seconds = 1
            self.timer_reset(timer, self.letter_counter)
        else:
            self.default_seconds = 3

        if self.timer_running:
            self.timer_tick(timer, messagebox)

    def timer_reset(self, timer, letter_counter):
        """reset"""
        self.letter_counter = letter_counter
        self.timer_seconds = self.default_seconds
        self.show_timer(timer)

    def timer_stop(self, timer):
        """stop"""
        self.timer_running = False
        self.show_timer(timer)

    def timer_tick(self, timer, messagebox):
        """tick"""
        if self.timer_running:
            self.show_timer(timer)
            timer.after(1000, self.timer_tick, timer, messagebox)
            if self.timer_seconds > 0:
                self.timer_seconds -= 1
            else:
                self.timer_stop(timer)
                messagebox.showinfo('Хорошая работа!',
                                    'Вы успели набрать {} симв. '
                                    '\nПродолжайте тренироваться!'
                                    .format(self.letter_counter))

    def show_timer(self, timer):
        """show"""
        timer['text'] = self.timer_seconds
