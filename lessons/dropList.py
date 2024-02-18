from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.menu import MDDropdownMenu

from quizzes.quiz_files.quiz_lib import DatabaseWorker


class dropList(MDApp):
    def build(self):
        self.x = DatabaseWorker('bitcoin_exchange_lesson.db')
        query = "SELECT * from users"
        results = self.x.search(query=query, multiple=True)
        self.users = results
        Window.size = (500, 700)

    def open_menu(self, drop_item_element):
        # self.menu_item = [c[1] for c in self.users]
        self.menu_item = []
        for c in self.users:
            name = c[1]
            self.menu_item.append(name)

        # Binding a function to a button (Callbacks)
        buttons_menu = []
        for it in self.menu_item:
            btn_dict = {"text":it,
                        "viewclass":"OneLineListItem",
                        "on_release": lambda x=it: self.button_pressed(x)
                        }
            # lambda tells the computer the following is an in_line function, which is a function that exists only in the line
            buttons_menu.append(btn_dict)

        self.menu = MDDropdownMenu(caller=drop_item_element, items=buttons_menu, width_mult=2)
        self.menu.open()

    def button_pressed(self, x):
        user = self.x.search(query=f"SELECT * from users where name='{x}'")
        if user:
            self.root.ids.customer.text = f"Customer {user[1]} with id{user[0]}"
            self.root.ids.dropdown_user.text = user[1]
        self.menu.dismiss()  # closes dropdown menu


test = dropList()
test.run()
test.x.close()