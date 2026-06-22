from flask import Blueprint, render_template, request, redirect, url_for

auth = Blueprint('auth', __name__)

# Login
@auth.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Authentication Logic Here
        return redirect(url_for('dashboard'))

    return render_template('login.html')


# Register
@auth.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Registration Logic Here
        return redirect(url_for('login'))

    return render_template('register.html')


# Logout
@auth.route('/logout')
def logout():

    return redirect(url_for('login'))