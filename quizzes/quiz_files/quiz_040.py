from kivymd.app import MDApp

class quiz_040(MDApp):
    def build(self):
        return

    def button_pressed(self):
        screen = self.root.ids.my_screen
        button = self.root.ids.my_button
        label = self.root.ids.my_label

        if screen.md_bg_color == [0, 0, 0, 1]:
            screen.md_bg_color = "white"
            button.md_bg_color = "black"
            button.text = "Dark Mode"
            label.text_color = "black"
        else:
            screen.md_bg_color = "black"
            button.md_bg_color = "white"
            button.text = "Light Mode"
            label.text_color = "white"



show = quiz_040()
show.run()