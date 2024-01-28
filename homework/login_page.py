from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen

class LoginScreen(MDScreen):
    def try_change(self):
        self.parent.current = 'register'
    pass

class RegisterScreen(MDScreen):
    def try_change(self):
        self.parent.current = 'login'
    pass

class login_page(MDApp):
    def build(self):
        Window.size = (600, 700)
        return


a = login_page()
a.run()