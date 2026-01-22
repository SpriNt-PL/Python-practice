import json

class ExpenseManager:
    filename = 'save.json'
    expences_list = []

    def addExpense(self):
        categories = ["Food", "Toy"]

        # Getting name
        while True:
            try:
                name = str(input("Enter the name of a product: "))
                break
            except ValueError:
                print("Incorrect value. Enter the name.")

        # Getting price
        while True:
            try:
                price = float(input("Enter the price: "))
                break
            except ValueError:
                print("Incorrect value. Enter the price.")

        # Printing all available categories
        print("Available product categories:")
        for c in categories:
            print(f"> {c}")
        
        # Getting category
        category = None
        while True:
            category = input("Enter the category: ")
            if category in categories:
                break
            else:
                print("Incorrect category")

        # Creating an expense
        expense = {
            "name" : name,
            "price" : price,
            "category" : category
        }

        # Saving an expense
        self.expences_list.append(expense)

        print("Expense added successfully")


    def listAllExpenses(self):
        for expense in self.expences_list:
            print(f"{expense['name']} belonging to the {expense['category']} collection was bought for {expense['price']}")

    
    def showStats(self):
        sum = 0
        for expense in self.expences_list:
            sum += expense['price']

        print(f"The sum of all expenses is equal to {sum}")


    def listOptions(self):
        print("Press proper number to:")
        print("0 -> Show all options")
        print("1 -> Add an expense")
        print("2 -> Show all expenses")
        print("3 -> Show statistics")
        print("4 -> Filter by a category")
        print("5 -> Exit")


    def saveToFile(self):
        with open(self.filename, 'w') as f:
            json.dump(self.expences_list, f)


    def loadFromFile(self):
         with open(self.filename, 'r') as f:
            data = json.load(f)
            self.expences_list = data

    def isCorrectYesNo(self, answer):
        possible_answers = ['Y', 'N']
        
        if answer in possible_answers:
            return True
        else:
            return False

            
print("Welcome to the expense manager.")

expense_manager = ExpenseManager()


answer = None
while not expense_manager.isCorrectYesNo(answer): 
    answer = input("Would you like to load the previous save? (Y/N): ")
    answer = answer.upper()

if answer == 'Y':
    expense_manager.loadFromFile()
    
expense_manager.listOptions()


while True:
    option = int(input("> "))

    match option:
        case 0:
            expense_manager.listOptions()
        case 1:
            expense_manager.addExpense()
        case 2:
            expense_manager.listAllExpenses()
        case 3:
            expense_manager.showStats()
        case 5:
            break

answer = None
while not expense_manager.isCorrectYesNo(answer): 
    answer = input("Would you like to save expenses? (Y/N): ")
    answer = answer.upper()

if answer == 'Y':
    expense_manager.saveToFile()

print("Goodbye")