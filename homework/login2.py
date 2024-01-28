from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen


class login2(MDApp):
    def build(self):
        Window.size = (600, 700)
        return


a = login2()
a.run()