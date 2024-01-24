# Universal Paper Clip Machine

from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.label import MDLabel

class MyLabel(MDLabel):
    pass

class clip_machine(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.money = 500
        self.wire = 50
        self.wire_price = 500
        self.clip = 0
    def build(self):
        Window.size = (500, 500)
        return

    def buy_wire(self):
        if self.money >= self.wire_price:
            self.wire += 10
            self.money -= self.wire_price
            self.root.ids.current_wire.text = f"{self.wire}m"
            self.root.ids.current_money.text = f"${self.money}"

    def make_clip(self):
        if self.wire >= 1:
            self.wire -= 1
            self.clip += 100
            self.root.ids.current_wire.text = f"{self.wire}m"
            self.root.ids.current_clips.text = f"{self.clip}"


show = clip_machine()
show.run()
