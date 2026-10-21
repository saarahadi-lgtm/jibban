# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 12:26:10 2026

@author: HP
"""
from config import CATEGORIES
from datetime import date


def read_text(prompt):
    """Ask the user for non-empty text."""
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("Text cannot be empty.")
        
        
def read_amount(prompt):
    """Ask the user for a positive whole number."""
    while True:
        text = input(prompt)

        try:
            amount = int(text.replace(",", ""))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if amount <= 0:
            print("Amount must be greater than zero.")
            continue

        return amount


def read_category():
    """Ask the user for a valid category."""
    while True:
        category = input(
            "Category (food/transport/bills/fun/other): "
        ).strip().lower()

        if category in CATEGORIES:
            return category

        print("Unknown category.")


def read_yes_no(question):
    while True:
        answer = input(question).strip().lower()

        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Please enter y or n.")


def read_date():
    """Ask the user for a valid date."""
    today = date.today().isoformat()

    while True:
        text = input(
            "Date (YYYY-MM-DD) [Enter = today]: "
        ).strip()

        if text == "":
            return today

        try:
            date.fromisoformat(text)
            return text
        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD.")
