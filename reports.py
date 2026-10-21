
# -*- coding: utf-8 -*-

from config import CATEGORIES
from datetime import date


def show_expenses(expenses):
    """Display all expenses in a table."""
    if len(expenses) == 0:
        print("No expenses yet.")
        return

    print(
        f"{'#':<4}{'Title':<20}{'Category':<12}"
        f"{'Amount':>12}{'Date':>15}"
    )
    print("-" * 63)

    for i, e in enumerate(expenses, start=1):
        print(
            f"{i:<4}{e.title:<20}"
            f"{e.category:<12}{e.amount:>12,}"
            f"{e.date:>15}"
        )


def calculate_total(expenses):
    """Return the total amount of expenses."""
    total = 0

    for e in expenses:
        total += e.amount

    return total


def calculate_total_sum(expenses):
    """Calculate total using sum()."""
    return sum(e.amount for e in expenses)


def count_expenses(expenses):
    """Return the number of expenses."""
    return len(expenses)


def calculate_average(expenses):
    """Return the average expense amount."""
    if len(expenses) == 0:
        return 0

    return calculate_total(expenses) / len(expenses)


def category_totals(expenses):
    """Calculate totals for each category."""
    totals = {}

    for e in expenses:
        cat = e.category
        totals[cat] = totals.get(cat, 0) + e.amount

    return totals


def find_most_expensive(expenses):
    """Return the most expensive expense."""
    if len(expenses) == 0:
        return None

    biggest = expenses[0]

    for e in expenses:
        if e.amount > biggest.amount:
            biggest = e

    return biggest


def find_cheapest(expenses):
    """Return the cheapest expense."""
    if len(expenses) == 0:
        return None

    cheapest = expenses[0]

    for e in expenses:
        if e.amount < cheapest.amount:
            cheapest = e

    return cheapest


def show_report(expenses):
    """Display a summary report."""
    print("========== REPORT ==========")

    if len(expenses) == 0:
        print("No expenses yet.")
        return

    biggest = find_most_expensive(expenses)
    cheapest = find_cheapest(expenses)

    print("Total:", f"{calculate_total(expenses):,}")
    print("Count:", count_expenses(expenses))
    print(f"Average: {calculate_average(expenses):,.0f}")

    print(
        "Most expensive:",
        biggest.title,
        f"{biggest.amount:,}"
    )

    print(
        "Cheapest:",
        cheapest.title,
        f"{cheapest.amount:,}"
    )

    totals = category_totals(expenses)
    total = calculate_total(expenses)

    for cat, amount in totals.items():
        percentage = amount / total * 100
        bar = "#" * (int(percentage) // 2)

        print(
            f"{cat:<12}{amount:>10,} "
            f"{percentage:>3.0f}% {bar}"
        )


def filter_by_month(expenses, month):
    """Return expenses belonging to a selected month."""
    try:
        date.fromisoformat(month + "-01")
    except (TypeError, ValueError):
        raise ValueError("Month must use YYYY-MM format.")

    return [
        e for e in expenses
        if e.date[:7] == month
    ]


def monthly_report(expenses):
    """Display a report for a selected month."""
    while True:
        month = input("Enter month (YYYY-MM): ").strip()

        try:
            date.fromisoformat(month + "-01")
            break
        except ValueError:
            print("Invalid month. Please use YYYY-MM.")

    monthly_expenses = filter_by_month(expenses, month)

    print(f"\nMonthly report for {month}")
    show_report(monthly_expenses)
