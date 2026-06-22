from flask import Blueprint, render_template, request, redirect, url_for
import sqlite3

expense = Blueprint('expense', __name__)

# Add Expense
@expense.route('/add', methods=['GET', 'POST'])
def add_expense():

    if request.method == 'POST':
        category = request.form['category']
        amount = request.form['amount']
        date = request.form['date']

        conn = sqlite3.connect("expense.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO expenses (category, amount, date) VALUES (?, ?, ?)",
            (category, amount, date)
        )

        conn.commit()
        conn.close()

        return redirect(url_for('dashboard'))

    return render_template('add_expense.html')


# Delete Expense
@expense.route('/delete/<int:id>')
def delete_expense(id):

    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM expenses WHERE id=?", (id,))

    conn.commit()
    conn.close()

    return redirect(url_for('dashboard'))