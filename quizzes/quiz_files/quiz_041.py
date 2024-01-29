# Tic Tac Toe Game, meant to be quiz 041

from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window

class MyButton(MDFlatButton):
    pass

class quiz_041(MDApp):
    def build(self):
        Window.size = (500, 500)
        turn = 0
        return

    def button_pressed_x(self, button):
        button.text = "X"
        button.md_bg_color = "#6d95fc"


show = quiz_041()
show.run()