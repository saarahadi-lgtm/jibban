 # -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 12:39:12 2026

@author: HP
"""
from config import CATEGORIES, DATA_FILE

from storage import load_expenses, save_expenses

from expenses import (
    add_expense,
    edit_expense,
    delete_expense,
    search_expenses
)

from reports import (
    show_expenses,
    calculate_total,
    calculate_total_sum,
    count_expenses,
    calculate_average,
    category_totals,
    find_most_expensive,
    find_cheapest,
    show_report,
    monthly_report
)

def show_menu():
    """Display the main menu."""
    print()
    print("=== Jibban - Personal Expense Tracker ===")
    print("1) Add expense")
    print("2) Show all expenses")
    print("3) Report")
    print("4) Search")
    print("5) Delete expense")
    print("6) Edit expense")
    print("7) Monthly report")
    print("0) Exit")


def main():
    expenses = load_expenses()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            show_expenses(expenses)

        elif choice == "3":
            show_report(expenses)

        elif choice == "4":
            search_expenses(expenses)

        elif choice == "5":
            delete_expense(expenses)

        elif choice == "6":
            edit_expense(expenses)

        elif choice == "7":
            monthly_report(expenses)

        elif choice == "0":
            print("Bye!")
            break

        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()
