
import unittest
from models import Expense
from reports import (
    calculate_total,
    count_expenses,
    calculate_average,
    category_totals
)


class TestExpenses(unittest.TestCase):

    def setUp(self):
        self.expenses = [
            Expense("Food", 100, "food", "2026-10-01"),
            Expense("Bus", 50, "transport", "2026-10-02")
        ]

    def test_calculate_total(self):
        self.assertEqual(calculate_total(self.expenses), 150)

    def test_count_expenses(self):
        self.assertEqual(count_expenses(self.expenses), 2)

    def test_calculate_average(self):
        self.assertEqual(calculate_average(self.expenses), 75)

    def test_category_totals(self):
        expenses = [
            Expense("Food", 100, "food", "2026-10-01"),
            Expense("Lunch", 50, "food", "2026-10-02"),
            Expense("Bus", 30, "transport", "2026-10-03")
        ]
        result = category_totals(expenses)
        self.assertEqual(result["food"], 150)
        self.assertEqual(result["transport"], 30)

    def test_empty_expenses(self):
        self.assertEqual(calculate_total([]), 0)
        self.assertEqual(count_expenses([]), 0)
        self.assertEqual(calculate_average([]), 0)
        self.assertEqual(category_totals([]), {})


if __name__ == "__main__":
    unittest.main()
