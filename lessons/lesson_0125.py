# Learning about screen managers
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen

class FirstScreen(MDScreen):
    def try_change(self):
        self.parent.current = 'Second'
    pass

class SecondScreen(MDScreen):
    pass

class multi_screen(MDApp):
    def build(self):
        Window.size = (400, 700)
        return


t = multi_screen()
t.run()