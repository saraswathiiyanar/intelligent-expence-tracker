class Expense:
    def __init__(self, expense_id, category, amount, date):
        self.expense_id = expense_id
        self.category = category
        self.amount = amount
        self.date = date

    def get_expense_details(self):
        return {
            "expense_id": self.expense_id,
            "category": self.category,
            "amount": self.amount,
            "date": self.date
        }