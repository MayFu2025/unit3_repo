class Account:
    def __init__(self):
        self.balance = 0
        self.holder_name = ""
        self.holder_email = ""
        self.number = ['000', '00000', '0']

    def get_account_no(self) -> str:
        separator = '-'
        output = separator.join(self.number)
        return output

    def set_holder_name(self, name:str) -> str:
        self.holder_name = name
        return f"Holder's name is {self.holder_name}"

    def set_holder_email(self, email:str) -> str:
        self.holder_email = email
        return f"Holder's email is {self.holder_email}"

    def get_balance(self) -> int:
        return self.balance

    def deposit(self, amount:int) -> str:
        self.balance += amount
        return f"New balance: {self.balance} USD"