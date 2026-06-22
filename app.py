from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = "secretkey123"

# ---------------- LOGIN ----------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == "admin" and password == "admin":
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            return "Invalid Login"

    return render_template('login.html')


# ---------------- REGISTER ----------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/profile')
def profile():
    return render_template('profile.html')


# ---------------- DASHBOARD ----------------
@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        conn = sqlite3.connect("expense.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM expenses")
        expenses = cursor.fetchall()

        conn.close()

        return render_template("dashboard.html", expenses=expenses)
    else:
        return redirect(url_for('login'))


# ---------------- ADD EXPENSE ----------------
@app.route('/add', methods=['GET', 'POST'])
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


# ---------------- ADVICE ----------------
@app.route('/advice')
def advice():
    return render_template("advice.html")

@app.route('/view')
def view_expenses():
    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()

    conn.close()

    return render_template("view_expenses.html", expenses=expenses)


# ---------------- INIT DB ----------------
def init_db():
    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        amount REAL,
        date TEXT
    )
    """)

    conn.commit()
    conn.close()


init_db()


if __name__ == "__main__":
    app.run(debug=True)