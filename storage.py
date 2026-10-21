# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 12:50:23 2026

@author: HP
"""

import json
from config import DATA_FILE
from models import Expense


def save_expenses(expenses):
    """Write the whole list to the JSON file."""
    data = [e.to_dict() for e in expenses]

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def expense_from_dict(d):
    """Convert a dictionary to an Expense object."""
    return Expense(
        d["title"],
        d["amount"],
        d["category"],
        d.get("date", "unknown")
    )


def load_expenses():
    """Read expenses from the JSON file."""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        return [expense_from_dict(d) for d in data]

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("File is corrupted, starting with an empty list.")
        return []
