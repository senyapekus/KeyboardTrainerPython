class Model:
    def __init__(self, text_file):
        self.text_file = text_file

    @property
    def text_file(self):
        return self.__text_file

    @text_file.setter
    def text_file(self, value):
        with open("text_speed_test.txt", "r", encoding='utf8') as file:
            self.__text_file = file.read().split('\n')
