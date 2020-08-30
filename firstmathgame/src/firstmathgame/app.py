"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class Firstmathgame(toga.App):


    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        math_label = toga.Label(
            'Task: ',
            style=Pack(padding=(0, 10), font_size=20)
        )
        self.user_input = toga.TextInput(style=Pack(flex=1))



        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(math_label)
        name_box.add(self.user_input)

        button = toga.Button(
            'Say Hello!',
            on_press=self.say_hello,
            style=Pack(padding=5)
        )

        main_box.add(name_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


    def say_hello(self, widget):
        print("Hello", self.user_input.value)
        self.user_input.text = "Hello {}!".format(self.name_input.value)

def main():
    return Firstmathgame()
