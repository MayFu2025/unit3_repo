from kivymd.app import MDApp

class quiz_040(MDApp):
    def build(self):
        self.count = 0
        return

    def button_pressed(self):
        self.count += 1
        label = self.root.ids.my_label
        label.text = f"Count {self.count}"

show = quiz_040()
show.run()