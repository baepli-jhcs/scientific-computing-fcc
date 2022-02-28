class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def get_name(self):
        return self.name

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction["amount"]
        return balance

    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        return False

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
        self.ledger.append({"amount": -amount, "description": description})
        return True

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, "Transfer to " + category.name)
        category.deposit(amount, "Transfer from " + self.name)
        return True

    def __str__(self):
        title = self.name.center(30, "*") + "\n"
        total = "Total: " + str(self.get_balance())
        items = ""
        for item in self.ledger:
            amount = "{:.2f}".format(item["amount"])
            length = 0
            if len(item["description"]) + len(amount) > 30:
                items += item["description"][: 29 - len(amount)] + " "
                length = len(item["description"][: 29 - len(amount)] + " ")
            else:
                items += item["description"]
                length = len(item["description"])
            items += format(amount, " >" + str(30 - length)) + "\n"
        return title + items + total


def create_spend_chart(categories):
    title = "Percentage spent by category\n"
    amounts = []
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])
        amounts.append(spent)
    total = sum(amounts)
    percentages = []
    for spending in amounts:
        percentages.append(int((spending / total) * 10) * 10)
    return_string_graph = title
    for i in range(100, -10, -10):
        temp_string = str(i) + "| "
        temp_string = temp_string.rjust(5)
        for percentage in percentages:
            if percentage >= i:
                temp_string += "o  "
            else:
                temp_string += "   "
        return_string_graph += temp_string + "\n"
    last_length = 0
    for percentage in percentages:
        last_length += 3
    return_string_graph += "    " + "-" * last_length + "-"
    label_lines = []
    for i in range(0, len(categories)):
        for j in range(0, len(categories[i].get_name())):
            try:
                while len(label_lines[j]) <= 3 * i - 3:
                    label_lines[j] += " "
                label_lines[j] += "  " + categories[i].get_name()[j]
            except:
                label_lines.append("   " * i + categories[i].get_name()[j])
    for i in range(0, len(label_lines)):
        label_lines[i] = label_lines[i].ljust(9)
        return_string_graph += "\n" + "     " + label_lines[i]
    return return_string_graph