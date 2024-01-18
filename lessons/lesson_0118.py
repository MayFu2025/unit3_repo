#the functionality of my_first_app goes in here

from kivymd.app import MDApp

class my_first_app(MDApp):
    def build(self):
        return

    def button_pressed(self):
        label = self.root.ids.my_label
        button = self.root.ids.my_button
        label.text = "The button was pressed."
        label.color = "red"
        button.text = "Oh no!"
        if button.md_bg_color == [0,0,1,1]:
            button.md_bg_color = "red"
        else:
            button.md_bg_color = "blue"



text = my_first_app()
text.run()