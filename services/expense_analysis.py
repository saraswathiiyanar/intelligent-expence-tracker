import sqlite3

class ExpenseAnalysis:

    @staticmethod
    def get_total_expense():
        conn = sqlite3.connect("expense.db")
        cursor = conn.cursor()

        cursor.execute("SELECT SUM(amount) FROM expenses")
        total = cursor.fetchone()[0]

        conn.close()

        return total if total else 0

    @staticmethod
    def get_total_transactions():
        conn = sqlite3.connect("expense.db")
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM expenses")
        count = cursor.fetchone()[0]

        conn.close()

        return count

    @staticmethod
    def get_category_expenses():
        conn = sqlite3.connect("expense.db")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT category, SUM(amount)
            FROM expenses
            GROUP BY category
        """)

        data = cursor.fetchall()

        conn.close()

        return data

    @staticmethod
    def get_highest_expense_category():
        conn = sqlite3.connect("expense.db")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT category, SUM(amount) as total
            FROM expenses
            GROUP BY category
            ORDER BY total DESC
            LIMIT 1
        """)

        result = cursor.fetchone()

        conn.close()

        return result