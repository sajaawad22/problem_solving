class Jar:
    def __init__(self):
        self.total_amount = 0
        self.components = {}

    def add(self, amount, component):
        if amount <= 0:
            return

        if component not in self.components:
            self.components[component] = 0

        self.components[component] += amount
        self.total_amount += amount

    def pour_out(self, amount):
        if amount <= 0 or self.total_amount == 0:
            return

        pour_ratio = amount / self.total_amount
        for component in list(self.components.keys()):
            self.components[component] -= self.components[component] * pour_ratio
            if self.components[component] < 0:
                self.components[component] = 0

        self.total_amount -= amount

        if self.total_amount < 0:
            self.total_amount = 0
            self.components = {}

    def get_concentration(self, component):
        if self.total_amount == 0 or component not in self.components:
            return 0
        return self.components[component] / self.total_amount

    def get_total_amount(self):
        return self.total_amount
