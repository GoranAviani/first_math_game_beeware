"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class Firstmathgame(toga.App):

    def __init__(self):
        super().__init__()
        self.counter = 0
        self.questions1 = [{'task': '1+1=', 'result': '2'}, {'task': '1+2=', 'result': '3'},
                           {'task': '1+3=', 'result': '4'},
                           {'task': '1+__=2', 'result': '1'}]
        self.task = self.questions1[self.counter]['task']
        self.result = self.questions1[self.counter]['result']

    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        self.math_label = toga.Label(
            'First math game:',
            style=Pack(padding=(0, 10))
        )
        self.task_display = toga.TextInput(style=Pack(flex=1))
        self.user_input = toga.TextInput(style=Pack(flex=1))


        math_box = toga.Box(style=Pack(direction=COLUMN, padding=5))
        math_box.add(self.math_label)
        math_box.add(self.task_display)
        math_box.add(self.user_input)

        button = toga.Button(
            'Submit answer!!',
            on_press=self.change_index(),
            style=Pack(padding=5)
        )

        main_box.add(math_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def change_index(self):
        print('change index!!!!!!!!!!!1')
        self.check_if_correct()
        self.counter += 1
        if self.counter > len(self.questions1):
            exit()
        self.tasks()

    def tasks(self):
        print('task!!!!!')
        #questions = {'1+1=': '2', '1+2=': '3', '1+3=': '4', '1+__=2': '1'}

        self.task = self.questions1[self.counter]['task']
        self.result = self.questions1[self.counter]['result']
        self.task_display.value = self.task

    def check_if_correct(self):
        print('check!!!!!!11')
        print(self.user_input.value)
        if self.user_input.value == self.result:
            print('Bravo!')
        else:
            print(":(")

def main():
    return Firstmathgame()
