# Tic Tac Toe Game

from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window

class MyButton(MDFlatButton):
    pass

class quiz_041(MDApp):
    def build(self):
        Window.size = (500, 500)
        self.turnA = True
        self.player_a = []
        self.player_b = []
        return

    def check_win(self):
        winner = None
        win = ["123", "456", "789", "147", "258", "369", "159", "357"]
        A = ''.join(self.player_a)
        B = ''.join(self.player_b)
        for i in win:
            if all(pos in A for pos in i):
                winner = "A"
            elif all(pos in B for pos in i):
                winner = "B"
        return winner

    def button_pressed(self, button):
        label = self.root.ids.turn_label
        if self.turnA:
            button.text = "X"
            button.md_bg_color = "#6d95fc"
            label.text = "Player B's Turn"
            self.player_a.append(str(button.name))
        elif not self.turnA:
            button.text = "O"
            button.md_bg_color = "#ffa59e"
            label.text = "Player A's Turn"
            self.player_b.append(str(button.name))
        self.turnA = not self.turnA

        check = self.check_win()
        if check == "A":
            label.text = "Player A Wins!"
            label.text_color = "#6d95fc"
            label.bold = True
            for i in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                self.root.ids[i].disabled = True
        elif check == "B":
            label.text = "Player B Wins!"
            label.text_color = "#ffa59e"
            label.bold = True
            for i in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                self.root.ids[i].disabled = True
        else:
            pass


show = quiz_041()
show.run()