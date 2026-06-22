from flask import Blueprint, render_template
import sqlite3

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/')
def home():

    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()

    total_expense = sum(expense[2] for expense in expenses)

    conn.close()

    return render_template(
        'dashboard.html',
        expenses=expenses,
        total_expense=total_expense
    )