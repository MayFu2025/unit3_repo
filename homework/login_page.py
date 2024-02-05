from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen

###DATABASE####
from login_lib import DatabaseWorker

# email = 'alice@xyz.com'
# password = 'pass123'
# username = 'alice'
# query = f"""INSERT into users(email, password, username)
#         values('{email}', '{password}', '{username}')
#         """
# db.insert(query=query)


###GUI####
class login_page(MDApp):
    def build(self):
        Window.size = (600, 700)
        db_name = 'login_system.db'
        db = DatabaseWorker(name=db_name)
        db.create()
        db.close()
        return

class LoginScreen(MDScreen):
    def try_change(self):
        self.parent.current = 'register'
    pass


class RegisterScreen(MDScreen):
    def try_change(self):
        self.parent.current = 'login'

    def try_signup(self):
        db_name = 'login_system.db'
        db = DatabaseWorker(name=db_name)

        success = False
        if self.ids.confirm_pass.text == self.ids.password.text:
            username = self.ids.username.text
            email = self.ids.email.text
            password = self.ids.password.text
            query = f"""INSERT into users(email, password, username)
                    values('{email}', '{password}', '{username}')
                    """
            db.insert(query=query)
            success = True
        return success


a = login_page()
a.run()

###GUI####