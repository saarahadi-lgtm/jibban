# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 09:53:00 2026

@author: HP
"""


class Expense:
    def __init__(self, title, amount, category, date):
        self.title = title
        self.amount = amount
        self.category = category
        self.date = date

    def __str__(self):
        return f"{self.date}  {self.title:<20}{self.amount:>12,}  ({self.category})"

    def to_dict(self):
        """Convert to a dict so json can save it."""
        return {
            "title": self.title,
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
        }
