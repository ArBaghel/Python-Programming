class BankAccount:
    def __init__(self):
        self.depositor_name = ""
        self.account_number = 0
        self.account_type = ""
        self.balance = 0.0

    def create_account(self):
        self.depositor_name = input("Enter depositor name: ")
        self.account_number = int(input("Enter account number: "))
        self.account_type = input("Enter account type: ")
        print("Account Created Successfully!")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful!")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful!")
        else:
            print("Insufficient balance or invalid withdrawal amount.")

    def inquire_balance(self):
        print("Balance: $", self.balance)

if __name__ == "__main__":
    account = BankAccount()

    while True:
        print("\nMenu:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Inquire Balance")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            account.create_account()
        elif choice == 2:
            deposit_amount = float(input("Enter amount to deposit: "))
            account.deposit(deposit_amount)
        elif choice == 3:
            withdraw_amount = float(input("Enter amount to withdraw: "))
            account.withdraw(withdraw_amount)
        elif choice == 4:
            account.inquire_balance()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


 