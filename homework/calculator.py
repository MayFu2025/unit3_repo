from kivymd.app import MDApp

class calculator(MDApp):
    def build(self):
        return

    def on_button_press(self, button_text):
        current_text = self.root.ids.input_field.text
        new_text = current_text + button_text
        self.root.ids.input_field.text = new_text

    def on_equals_press(self):
        try:
            result = str(eval(self.root.ids.input_field.text))
            self.root.ids.input_field.text = result
        except Exception as e:
            self.root.ids.input_field.text = 'Error'

    def on_ac_press(self):
        self.root.ids.input_field.text = ''

    def on_plusminus_press(self):
        self.root.ids.input_field.text = str(eval(self.root.ids.input_field.text) * -1)

    def on_percent_press(self):
        self.root.ids.input_field.text = str(eval(self.root.ids.input_field.text) * 0.01)


text = calculator()
text.run()