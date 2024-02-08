import sqlite3

from kivymd.app import MDApp
from quiz_lib import DatabaseWorker

class quiz_046(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.components = {"base":0, "health":0, "pension":0, "income_tax":0, "inhabitant":0, "total":0, "hash":""}
        self.db_connection = DatabaseWorker('payments.db')
    def build(self):
        return

    def save(self):
        pass

    def update(self):
        #This function updates all the labels in the form using the base salary and the percentage
        # Pseudocode
        # 1- get the base salary from the GUI
        # 2- if base salary define total=int(base) and an empty string to store build a hash (for_hash="") if no base then end the function
        # 3- for Each TextField with ids: "inhabitant","income_tax","pension","health" get the text property
        # 4- if the TextField.text has a number (value), calculate the equation new_value="(base*int(value)//100) JPY" and subbctract the equation to the total
        # 5- if no: then new_value = " JPY"
        # 6- set the label next to the TextField (inhabitant_label, income_tax_label, etc) to the variable new_value
        # 7- concatenate to the hash variable the f"{id}{value}"
        # 8- set the text of the element id=total to the total with the JPY symbol
        # 9- encrypt the hash and change the text of the label with id=hash to the last 50 characters of the hash

        base = self.root.ids.base.text

        if base:
            base_int = int(base)  # Why not define as total
            hash = ""

            inhabitant = int(self.root.ids.inhabitant.text or '0')  # or 0 takes 0 if none
            income_tax = int(self.root.ids.income_tax.text or '0')
            pension = int(self.root.ids.pension.text or '0')
            health = int(self.root.ids.inhabitant.text or '0')

            pension_jpy = base_int * (pension//100)
            inhabitant_jpy = base_int * (inhabitant // 100)
            income_tax_jpy = base_int * (income_tax // 100)
            health_jpy = base_int * (health // 100)
            total = base_int - pension_jpy - inhabitant_jpy - income_tax_jpy - health_jpy

            self.root.ids.pension_label.text = f"{pension_jpy} JPY"
            self.root.ids.income_tax_label.text = f"{income_tax} JPY"
            self.root.ids.inhabitant_label.text = f"{inhabitant_jpy} JPY"
            self.root.ids.health_label.text = f"{health} JPY"
            self.root.ids.salary_label.text = f"{total} JPY"

            hash = f"base{base_int},inhabitant{inhabitant},income_tax{income_tax},pension{pension},health{health},total{total}"

            # Putting data inside self is called encapsulation (opposite is called decapsulation)
            self.components["base"] = base_int
            self.components["pension"] = pension
            self.components["health"] = health
            self.components["inhabitant"] = inhabitant
            self.components["income_tax"] = income_tax
            self.components["total"] = total
            self.components["hash"] = hash

        #calculate total
            ids = ["inhabitant", "income_tax", "pension", "health"]

        # update the percentage

        else:
            pass

    def save(self):
        #repeat the algorithm in update but create variables to save the amount of each item:
        #base = int(base)
        #inhabitant = amount in JPY to remove from base for inhabitant tax
        #income_tax = amount in JPY to remove from base for income tax
        #pension = amount in JPY to remove from base for pension tax
        #health = amount in JPY to remove from base for health tax
        #total = total net salary
        #hahs = hash of the calcualtions in the format
        #inhabitant4,income_tax3,pension2,health1,total1103  (here the numbers next to the category are percentages)

        base_int = self.components["base"]
        pension = self.components["pension"]
        health = self.components["health"]
        inhabitant = self.components["inhabitant"]
        income_tax = self.components["income_tax"]
        total = self.components["total"]
        hash_str = self.components["hash"]

        query = f"""INSERT into payments(base, inhabitant, income_tax, pension, health, total, hash)
        values({base_int}, {inhabitant}, {income_tax}, {pension}, {health}, {total}, '{DatabaseWorker.make_hash(text=hash_str)}') 
        """

        db.run_query(query)
        db.close()
        self.root.ids.hash.text = f"Payment saved"

    def clear(self):
        for label in ["base", "inhabitant","income_tax","pension","health"]:
            self.root.ids[label].text = ""
            self.root.ids[label+"_label"].text = " JPY"

        self.root.ids["salary_label"].text = " JPY"
        self.root.ids.hash.text = "----"


test = quiz_046()
drop = """Drop table if exists payments"""
create = """CREATE TABLE if not exists payments(
        id integer primary key,
        base int,
        health int,
        pension int,
        income_tax int,
        inhabitant int,
        total int,
        hash text
 )"""
db = DatabaseWorker("payments.db")
db.run_query(create)

test.run()
test.db_connection.close()