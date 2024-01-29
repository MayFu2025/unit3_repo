class Compound_Interest:
    def __init__(self):
        self.principal = None
        self.rate = None
        self.n_years = None

    def set_principal(self, principal):
        self.principal = principal
    def set_rate(self, rate):
        self.rate = rate
    def set_years(self, n_years:int):
        self.n_years = n_years

    def calculate_interest(self):
        return self.principal * ((1+self.rate) ** self.n_years)


class AccountingProgram(Compound_Interest):
    def __init__(self):
        super(AccountingProgram, self).__init__()
        self.customer_name = None
        self.customer_email = None

    def set_customer_name(self, customer_name):
        self.customer_name = customer_name

    def set_customer_email(self, customer_email):
        self.customer_email = customer_email
    def get_message(self):
        return f"{self.customer_name} will have {self.calculate_interest():.2f} USD in {self.n_years} years if the principal is {self.principal} USD with {self.rate*100}% annual compound interest."


May = Accounting()
May.set_principal(1000)
May.set_rate(0.05)
May.set_years(10)
print(May.get_message())