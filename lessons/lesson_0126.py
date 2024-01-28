from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout


class MyButton(MDBoxLayout):
    pass

class twofoureight(MDApp):
    def build(self):
        Window.size = 500, 700
        return

    def button_pressed(self, btn):
        pass


t = twofoureight()
t.run()