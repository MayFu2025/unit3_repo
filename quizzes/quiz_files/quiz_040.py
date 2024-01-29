from kivymd.app import MDApp

class quiz_040(MDApp):
    def build(self):
        return

    def button_pressed(self):
        button = self.root.ids.my_button

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