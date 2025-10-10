import unittest
from ExpenseTracker import Expense, ExpenseTracker

class TestExpense(unittest.TestCase):
    def test_create_valid_expense(self):
        e = Expense("Lunch", 12.5)
        self.assertEqual(e.description, "Lunch")
        self.assertEqual(e.amount, 12.5)

    def test_negative_expense_raises_error(self):
        with self.assertRaises(ValueError):
            Expense("Invalid", -10)


class TestExpenseTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = ExpenseTracker()

    def test_add_expense(self):
        self.tracker.add_expense("Coffee", 4.5)
        self.assertEqual(len(self.tracker.expenses), 1)
        self.assertEqual(self.tracker.expenses[0].amount, 4.5)

    def test_calculate_total(self):
        self.tracker.add_expense("Lunch", 10)
        self.tracker.add_expense("Dinner", 20)
        total = self.tracker.calculate_total()
        self.assertEqual(total, 30)

    def test_total_zero_if_no_expenses(self):
        self.assertEqual(self.tracker.calculate_total(), 0)


if __name__ == "__main__":
    unittest.main()
