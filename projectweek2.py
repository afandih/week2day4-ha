class BudgetTracker:

    def __init__(self):
        self.balance = 0

    def add_income(self, amount):
        if amount > 0:
            self.balance += amount
            print("Income added successfully.")
        else:
            print("Invalid income amount.")

    def add_expense(self, amount):
        if amount > 0:
            self.balance -= amount
            print("Expense recorded.")
        else:
            print("Invalid expense amount.")

    def show_balance(self):
        print("Current Balance:", self.balance)


print("Welcome to the Budget Tracker!")

tracker = BudgetTracker()

while True:
    print("\n--- Budget Tracker Menu ---")
    print("1. Add income")
    print("2. Add expense")
    print("3. Show balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter income amount: "))
        tracker.add_income(amount)

    elif choice == "2":
        amount = float(input("Enter expense amount: "))
        tracker.add_expense(amount)

    elif choice == "3":
        tracker.show_balance()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")