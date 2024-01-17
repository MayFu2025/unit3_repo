from matplotlib import pyplot as plt
import random

class SalemanMap:
    def __init__(self):
        self.x = []
        self.y = []
        self.name = None

    def get_map(self):

        for n in range(len(self.name)):
            plt.plot((self.x[n]), (self.y[n]), marker="o", label=self.name[n])
        plt.show()

    def generate_data(self, names:list):
        self.name = names
        for i in names:
            self.x.append(random.randint(0,100))
            self.y.append(random.randint(0,100))


# x: list[int], y: list[int], name: list[str]

test = SalemanMap()
test.generate_data(['Kobe', 'Tokyo', 'Nagoya', 'Kyoto', 'Saitama', "Yokohama"])
test.get_map()
