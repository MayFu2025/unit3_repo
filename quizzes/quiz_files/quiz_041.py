# Tic Tac Toe Game, meant to be quiz 041

from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window

class MyButton(MDFlatButton):
    pass

class quiz_042(MDApp):
    def build(self):
        Window.size = (500, 500)
        return

    def button_pressed(self, button):
        button.text = "pressed"
        button.md_bg_color = "#002aff"


show = quiz_042()
show.run()