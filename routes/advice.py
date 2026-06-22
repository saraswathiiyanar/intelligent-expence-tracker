from flask import Blueprint, render_template
import sqlite3

advice = Blueprint('advice', __name__)

@advice.route('/advice')
def financial_advice():

    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]

    conn.close()

    if total is None:
        advice_message = "Start tracking your expenses regularly."

    elif total > 10000:
        advice_message = "Your spending is high. Try to reduce unnecessary expenses."

    elif total > 5000:
        advice_message = "Maintain a monthly budget to improve savings."

    else:
        advice_message = "Good job! Your expenses are under control."

    return render_template(
        "financial_advice.html",
        advice=advice_message
    )