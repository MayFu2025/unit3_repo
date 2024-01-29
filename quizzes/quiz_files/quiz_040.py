from kivymd.app import MDApp

class quiz_040(MDApp):
    def build(self):
        return

    def button_pressed(self):
        screen = self.root.ids.my_screen
        button = self.root.ids.my_button

        if screen.md_bg_color == "#ffffff":
            screen.md_bg_color = "#000000"
        else:
            screen.md_bg_color = "#ffffff"

        if button.text == "Dark Mode":
            button.text = "Light Mode"
        else:
            button.text = "Dark Mode"

        if button.md_bg_color == [0, 0, 0, 1]:
            button.md_bg_color = "white"
        else:
            button.md_bg_color = "black"


show = quiz_040()
show.run()