class Expense:
    """
    Save an expense record.
    """
    def __init__(self, description: str, amount: float):
        if amount < 0:
            raise ValueError("Expense amount cannot be negative.")
        self.description = description
        self.amount = amount


class ExpenseTracker:
    """
    Tracks multiple expenses and provides functionality to
    add expenses and calculate the total.
    """
    def __init__(self):
        self.expenses = []

    def add_expense(self, description: str, amount: float):
        expense = Expense(description, amount)
        self.expenses.append(expense)

    def calculate_total(self) -> float:
        return sum(expense.amount for expense in self.expenses)

    def display_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
        else:
            for exp in self.expenses:
                print(f"{exp.description}: ${exp.amount:.2f}")
            print(f"Total: ${self.calculate_total():.2f}")


if __name__ == "__main__":
    tracker = ExpenseTracker()

    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. Show Total")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            desc = input("Enter expense description: ")
            amt = float(input("Enter amount: "))
            tracker.add_expense(desc, amt)
            print("Expense added successfully.")

        elif choice == "2":
            tracker.display_expenses()

        elif choice == "3":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
