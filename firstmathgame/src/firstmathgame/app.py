"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class Firstmathgame(toga.App):


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
            on_press=self.tasks(),
            style=Pack(padding=5)
        )

        main_box.add(math_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def tasks(self):
        questions = {'1+1=': '2', '1+2=': '3', '1+3=': '4', '1+__=2': '1'}
        for self.task, self.result in questions.items():
            self.task_display.value = self.task
            result1 = self.check_if_correct()
            print(result1)



    def check_if_correct(self):
        self.user_input.text = "Hello {}!".format(self.user_input.value)
        if self.user_input.value == self.result:
            print('Bravo!')
        else:
            print(":(")
        return 'a'

def main():
    return Firstmathgame()
