# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 13:11:16 2026

@author: HP
"""

from config import CATEGORIES
from inputs import (
    read_text,
    read_amount,
    read_category,
    read_date,
    read_yes_no
)
from storage import save_expenses
from reports import show_expenses
from models import Expense


def add_expense(expenses):
    """Read a new expense and append it to the list."""
    title = read_text("Title: ")
    amount = read_amount("Amount (Toman): ")
    category = read_category()
    expense_date = read_date()

    expense = Expense(
        title,
        amount,
        category,
        expense_date
    )

    expenses.append(expense)
    save_expenses(expenses)
    print("Saved!")


def edit_expense(expenses):
    """Edit an existing expense."""
    if len(expenses) == 0:
        print("No expenses to edit.")
        return

    show_expenses(expenses)

    try:
        row_number = int(input("Row number to edit: "))
    except ValueError:
        print("Invalid row number.")
        return

    index = row_number - 1

    if index < 0 or index >= len(expenses):
        print("Invalid row number.")
        return

    expense = expenses[index]

    new_title = input(
        f"Title [{expense.title}]: "
    ).strip()

    if new_title:
        expense.title = new_title

    new_amount = input(
        f"Amount [{expense.amount}]: "
    ).strip()

    if new_amount:
        try:
            new_amount = int(new_amount.replace(",", ""))
        except ValueError:
            print("Please enter a whole number.")
            return

        if new_amount > 0:
            expense.amount = new_amount
        else:
            print("Amount must be greater than zero.")
            return

    new_category = input(
        f"Category [{expense.category}]: "
    ).strip().lower()

    if new_category:
        if new_category in CATEGORIES:
            expense.category = new_category
        else:
            print("Unknown category.")
            return

    print(
        f"Updated: {expense.title} | "
        f"{expense.amount:,} | "
        f"{expense.category}"
    )

    save_expenses(expenses)


def delete_expense(expenses):
    """Delete an expense from the list."""
    if len(expenses) == 0:
        print("No expenses to delete.")
        return

    show_expenses(expenses)

    try:
        row_number = int(input("Row number to delete: "))
    except ValueError:
        print("Invalid row number.")
        return

    index = row_number - 1

    if index < 0 or index >= len(expenses):
        print("Invalid row number.")
        return

    expense = expenses[index]

    if read_yes_no(f'Delete "{expense.title}"? (y/n): '):
        del expenses[index]
        save_expenses(expenses)
        print("Deleted!")
    else:
        print("Cancelled.")


def search_expenses(expenses):
    """Search expenses by title."""
    keyword = input("Search: ").strip().lower()

    found = False

    for e in expenses:
        if keyword in e.title.lower():
            print(e.title)
            found = True

    if not found:
        print("Nothing found")

