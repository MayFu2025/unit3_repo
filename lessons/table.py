# Making a table in Kivy

from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen
from quizzes.quiz_files.quiz_lib import DatabaseWorker, make_hash

class TableScreen(MDScreen):
    # db = DatabaseWorker('bitcoin_exchange_lesson.db')  # Class variable: same for all objects of the class
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_tables = None
        self.selected_rows = []  # List to keep track which rows were selected
    def on_pre_enter(self, *args): #'*args' means it doesn't know what the arguments will be
        columns_names = [('id', 50), ('Sender', 50), ('Receiver', 50), ('Amount', 50), ('Signature', 100)]
        self.data_tables = MDDataTable(
            size_hint = (0.8, 0.5),
            pos_hint = {'center_x':0.5, 'center_y':0.5},
            use_pagination = False,
            check = True,
            column_data = columns_names
        )
        self.data_tables.bind(on_row_press=self.row_pressed)  # bind a function to function
        self.data_tables.bind(on_check_press=self.checkbox_pressed)
        self.add_widget(self.data_tables)
        self.update()

    def update(self):
        data = table.db.search(query='Select * from ledger', multiple=True)
        self.data_tables.update_row_data(None, data)

    def row_pressed(self, table, cell):
        print(f"Value clicked: {cell.text}")

    def checkbox_pressed(self, table, current_row):
        print(f"Record checked: {current_row}")
        # Here you could delete or update the record

    def save(self):
        sender = self.ids.sender.text
        receiver = self.ids.receiver.text
        amount = self.ids.amount.text
        signature = f"sender_id {sender}, receiver_id {receiver},amount {amount}"

        query = f'''insert into ledger(sender_id, receiver_id, amount, signature)
                    values({sender}, {receiver}, {amount}, {make_hash(signature)})'''
        table.db.run_query(query)

class table(MDApp):
    db = DatabaseWorker('bitcoin_exchange_lesson.db')
    def build(self):
        pass


app = table()
app.run()
app.db.close()