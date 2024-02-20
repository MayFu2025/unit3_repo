# Quiz 046
<hr>

### Prompt
![](images/quiz_046_slide.png)
*fig. 1* **Screenshot of quiz slides**

### Solution
Python file
```.py
from kivymd.app import MDApp
from quiz_lib import DatabaseWorker, make_hash, check_text

# HL: Check validity of database entries
def check_frauds():
    output = []
    query = "select * from payments"
    data = db.search(query, multiple=True)
    print(data)
    for row in data:
        text = f"base{row[1]},inhabitant{row[2]},income_tax{row[3]},pension{row[4]},health{row[5]},total{row[6]}"
        if not check_text(text=text, hashed=row[7]):
            output.append(f"Signature mismatch: transaction id {row[0]}")
    return output
    
 class quiz_046(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.components = {"base":0, "health":0, "pension":0, "income_tax":0, "inhabitant":0, "total":0, "hash":""}
        self.db_connection = DatabaseWorker('payments.db')
    def build(self):
        return

    def update(self):
        base = self.root.ids.base.text
        if base:
            base_int = int(base)
            health = int(self.root.ids.health.text or '0')
            pension = int(self.root.ids.pension.text or '0')
            income_tax = int(self.root.ids.income_tax.text or '0')
            inhabitant = int(self.root.ids.inhabitant.text or '0')

            health_jpy = base_int * health // 100
            self.root.ids.health_label.text = f"{health_jpy} JPY"

            pension_jpy = base_int * pension // 100
            self.root.ids.pension_label.text = f"{pension_jpy} JPY"

            income_tax_jpy = base_int * income_tax // 100
            self.root.ids.income_tax_label.text = f"{income_tax_jpy} JPY"

            inhabitant_jpy = base_int * inhabitant // 100
            self.root.ids.inhabitant_label.text = f"{inhabitant_jpy} JPY"

            total = base_int - pension_jpy - health_jpy - income_tax_jpy - inhabitant_jpy
            self.root.ids.salary_label.text = f"{total} JPY"

            to_hash = f"base{base_int},inhabitant{inhabitant_jpy},income_tax{income_tax_jpy},pension{pension_jpy},health{health_jpy},total{total}"

            # Putting data inside self is called encapsulation (opposite is called decapsulation)
            self.components["base"] = base_int
            self.components["pension"] = pension_jpy
            self.components["health"] = health_jpy
            self.components["inhabitant"] = inhabitant_jpy
            self.components["income_tax"] = income_tax_jpy
            self.components["total"] = total
            self.components["hash"] = make_hash(text=to_hash)

            self.root.ids.hash.text = self.components["hash"][-50:]

        else:
            pass

    def save(self):
        base_int = self.components["base"]
        pension = self.components["pension"]
        health = self.components["health"]
        inhabitant = self.components["inhabitant"]
        income_tax = self.components["income_tax"]
        total = self.components["total"]
        hash_str = self.components["hash"]

        query = f"""INSERT into payments(base, inhabitant, income_tax, pension, health, total, hash)
        values({base_int}, {inhabitant}, {income_tax}, {pension}, {health}, {total}, '{hash_str}') 
        """

        db.run_query(query)
        self.root.ids.hash.text = f"Payment saved"
        print(check_frauds())
        db.close()

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
```

Kivy file
```.kv
MDScreen:
    id:bck
    size: 200, 500

    MDBoxLayout:
        id: bck
        size_hint: .8,.9
        md_bg_color: "#F2F2F2"
        orientation: "vertical"
        pos_hint: {"center_x":.5, "center_y":.5}
        spacing: dp(10)

        MDLabel:
            text:"Compensation Calculator"
            halign: "center"
            font_style:"H4"
            color: "#222222"

        MDBoxLayout:
            size_hint_x: .8
            height: dp(46)
            valign: "center"
            md_bg_color: "#FFFFFF"
            pos_hint: {"center_x":.5, "center_y":.5}
            spacing: dp(10)

            MDIcon:
                icon: "plus-circle"
                pos_hint: {"center_x": .5, "center_y": .5}
            MDLabel:
                text:"Base Salary"
                size_hint_x: .4
            MDTextField:
                id:base
                mode: "rectangle"
                input_filter:"int"
                text_color_normal: "#222222"
                line_color_normal: "#222222"
                hint_text: "Base Salary"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_text:
                    root.ids.base_label.text = f"{self.text} JPY"
                    app.update()
            MDLabel:
                id: base_label
                text:" JPY"

        MDBoxLayout:
            size_hint_x: .8
            height: dp(46)
            valign: "center"
            md_bg_color: "#FFFFFF"
            pos_hint: {"center_x":.5, "center_y":.5}
            spacing: dp(10)


            MDIcon:
                icon: "minus-circle"
                pos_hint: {"center_x": .5, "center_y": .5}
                color: "#9d0208"
            MDLabel:
                text:"Health"
                size_hint_x: .4
                color: "#6a040f"
            MDTextField:
                id:health
                mode: "rectangle"
                input_filter:"int"
                hint_text: "% Health"
                pos_hint: {"center_x": .5, "center_y": .5}
                text_color_normal: "#9d0208"
                line_color_normal: "#9d0208"
                on_text:
                    self.text = str(max(0, min(100, int(self.text or 0))))
                    app.update()
            MDLabel:
                id: health_label
                text:" JPY"
                color: "#9d0208"

        MDBoxLayout:
            size_hint_x: .8
            height: dp(46)
            valign: "center"
            md_bg_color: "#FFFFFF"
            pos_hint: {"center_x":.5, "center_y":.5}
            spacing: dp(10)


            MDIcon:
                icon: "minus-circle"
                pos_hint: {"center_x": .5, "center_y": .5}
                color: "#9d0208"
            MDLabel:
                text: "Pension"
                size_hint_x: .4
                color: "#9d0208"
            MDTextField:
                id:pension
                mode: "rectangle"
                input_filter:"int"
                hint_text: "% Pension"
                text_color_normal: "#9d0208"
                line_color_normal: "#9d0208"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_text:
                    self.text = str(max(0, min(100, int(self.text or 0))))
                    app.update()
            MDLabel:
                id: pension_label
                text:" JPY"
                color: "#9d0208"


        MDBoxLayout:
            size_hint_x: .8
            height: dp(46)
            valign: "center"
            md_bg_color: "#FFFFFF"
            pos_hint: {"center_x":.5, "center_y":.5}
            spacing: dp(10)

            MDIcon:
                icon: "minus-circle"
                pos_hint: {"center_x": .5, "center_y": .5}
                color: "#9d0208"
            MDLabel:
                text:"Income Tax"
                size_hint_x: .4
                color: "#9d0208"
            MDTextField:
                id:income_tax
                mode: "rectangle"
                input_filter:"int"
                hint_text: "% Income"
                text_color_normal: "#9d0208"
                line_color_normal: "#9d0208"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_text:
                    self.text = str(max(0, min(100, int(self.text or 0))))
                    app.update()
            MDLabel:
                id: income_tax_label
                text:" JPY"
                color: "#9d0208"

        MDBoxLayout:
            size_hint_x: .8
            height: dp(46)
            valign: "center"
            md_bg_color: "#FFFFFF"
            pos_hint: {"center_x":.5, "center_y":.5}
            spacing: dp(10)


            MDIcon:
                icon: "minus-circle"
                pos_hint: {"center_x": .5, "center_y": .5}
                color: "#9d0208"
            MDLabel:
                text:"Inhabitant Tax"
                size_hint_x: .4
                color: "#9d0208"
            MDTextField:
                id:inhabitant
                mode: "rectangle"
                input_filter:"int"
                hint_text: "%  Income"
                text_color_normal: "#9d0208"
                line_color_normal: "#9d0208"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_text:
                    self.text = str(max(0, min(100, int(self.text or 0))))
                    app.update()
            MDLabel:
                id: inhabitant_label
                text:" JPY"
                color: "#9d0208"


        MDBoxLayout:
            size_hint_x: .8
            height: dp(46)
            valign: "center"
            md_bg_color: "#22223b"
            pos_hint: {"center_x":.5, "center_y":.5}
            spacing: dp(10)

            MDLabel:
                size_hint_x: .5
            MDIcon:
                icon: "calculator"
                pos_hint: {"center_x": .5, "center_y": .5}
                color: "#F2F2F2"
            MDLabel:
                text:"Net Salary"
                size_hint_x: .4
                color: "#F2F2F2"
            MDLabel:
                id: salary_label
                text:" JPY"
                color: "#F2F2F2"
            MDFloatingActionButton:
                icon:"content-save-plus"
                md_bg_color:"#ffc300"
                icon_color:"#222222"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_press:
                    app.save()

            MDFloatingActionButton:
                icon:"autorenew"
                md_bg_color:"#2a9d8f"
                icon_color:"#222222"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_press:
                    app.clear()

        MDBoxLayout:
            size_hint: .8, .2
            valign: "center"
            md_bg_color: "#FFFFFF"
            pos_hint: {"center_x":.5, "center_y":.5}

            MDLabel:
                id: hash
                halign: "center"
                text: "----"
                font_style: "Caption"
```

### Evidence


https://github.com/MayFu2025/unit3_repo/assets/122759229/807a6a1d-43eb-41fe-a481-cf4d1861e11e


*fig. 2* **Video of popup screen**

### UML Diagram
![](images/quiz_046_diagram1.jpeg)
*fig. 3* **UML Diagram for solution**

### ER diagram
![](images/quiz_046_diagram2.png)
*fig. 3* **ER diagram for `payments`**