# Meant to be quiz 42

from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen

class quiz_042(MDApp): #Meant to be named mystery
    def build(self):
        Window.size = (400, 700)
        return

class MysteryPageA(MDScreen):
    def message1(self):
        self.parent.current = 'Second'
    pass

class MysteryPageB(MDScreen):
    def message2(self):
        self.parent.current = 'First'

t = quiz_042()
t.run()