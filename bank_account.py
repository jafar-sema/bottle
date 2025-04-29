class BankAccount:
    def __init__(self, owner, balance=0):
        """Initialize a BankAccount object with owner's name and balance."""
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} into {self.owner}'s account.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if self.balance >= amount > 0:
            self.balance -= amount
            print(f"Withdrew {amount} from {self.owner}'s account.")
        else:
            print("Invalid withdrawal amount or insufficient funds!")

    def transfer(self, recipient, amount):
        """Transfer money from this account to another account."""
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            print(f"Transferred {amount} from {self.owner}'s account to {recipient.owner}'s account.")
        else:
            print("Invalid transfer amount or insufficient funds!")

    def get_balance(self):
        """Get the current balance of the account."""
        return self.balance

    def __str__(self):
        """Return a string representation of the account."""
        return f"Account owner: {self.owner}\nAccount balance: {self.balance}"


def main():
    """Main function to demonstrate the banking system."""
    print("Welcome to the Banking System!")
    # Create two bank accounts
    account1 = BankAccount("Alice", 1000)
    account2 = BankAccount("Bob")

    print(account1)
    print(account2)

    # Deposit and withdraw money from the accounts
    account1.deposit(500)
    account2.deposit(100)

    account1.withdraw(200)
    account2.withdraw(50)

    # Transfer money between accounts
    account1.transfer(account2, 300)

    print("\nFinal Account Details:")
    print(account1)
    print(account2)


if __name__ == "__main__":
    main()
