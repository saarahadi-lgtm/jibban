
# -*- coding: utf-8 -*-

import unittest

from models import Expense
from reports import (
    calculate_total,
    count_expenses,
    calculate_average,
    category_totals,
    filter_by_month,
)


class TestExpenses(unittest.TestCase):

    def setUp(self):
        self.expenses = [
            Expense("Lunch", 200, "food", "2026-10-01"),
            Expense("Bus", 50, "transport", "2026-10-02"),
            Expense("Dinner", 300, "food", "2026-09-30"),
        ]

    # Test 1: Total
    def test_calculate_total(self):
        self.assertEqual(calculate_total(self.expenses), 550)

    # Test 2: Empty list
    def test_calculate_total_empty(self):
        self.assertEqual(calculate_total([]), 0)

    # Test 3: One expense
    def test_calculate_total_one_expense(self):
        expenses = [
            Expense("Coffee", 80, "food", "2026-10-03")
        ]
        self.assertEqual(calculate_total(expenses), 80)

    # Test 4: Count
    def test_count_expenses(self):
        self.assertEqual(count_expenses(self.expenses), 3)

    # Test 5: Empty count
    def test_count_expenses_empty(self):
        self.assertEqual(count_expenses([]), 0)

    # Test 6: Average
    def test_calculate_average(self):
        self.assertAlmostEqual(
            calculate_average(self.expenses),
            550 / 3
        )

    # Test 7: Empty average
    def test_calculate_average_empty(self):
        self.assertEqual(calculate_average([]), 0)

    # Test 8: Category totals
    def test_category_totals(self):
        self.assertEqual(
            category_totals(self.expenses),
            {"food": 500, "transport": 50}
        )

    # Test 9: One category
    def test_category_totals_one_category(self):
        expenses = [
            Expense("Lunch", 200, "food", "2026-10-01"),
            Expense("Dinner", 300, "food", "2026-10-02"),
        ]

        self.assertEqual(
            category_totals(expenses),
            {"food": 500}
        )

    # Test 10: Empty category totals
    def test_category_totals_empty(self):
        self.assertEqual(category_totals([]), {})

    # Test 11: Filter by month
    def test_filter_by_month(self):
        result = filter_by_month(self.expenses, "2026-10")

        self.assertEqual(
            [e.title for e in result],
            ["Lunch", "Bus"]
        )

    # Test 12: Month without expenses
    def test_filter_month_with_no_expenses(self):
        result = filter_by_month(self.expenses, "2026-08")

        self.assertEqual(result, [])

    # Test 13: Empty list with month filter
    def test_filter_by_month_empty_list(self):
        self.assertEqual(
            filter_by_month([], "2026-10"),
            []
        )

    # Test 14: Invalid month
    def test_filter_by_month_invalid_month(self):
        with self.assertRaises(ValueError):
            filter_by_month(self.expenses, "2026-13")


if __name__ == "__main__":
    unittest.main()
