class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdrawal successful")

    def show_balance(self):
        print("Balance:", self.balance)


account = BankAccount(0)

while True:

    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)

    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)

    elif choice == 3:
        account.show_balance()

    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")