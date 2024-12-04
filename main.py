from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Secret key for session protection
app.secret_key = '1a2b3c4d5e6d7g8h9i10'

# Database connection details
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''  # Replace with your MySQL password
app.config['MYSQL_DB'] = 'loginapp'

# Initialize MySQL
mysql = MySQL(app)


# Login page
@app.route('/pythonlogin/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        # Check if account exists
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()

        if account and check_password_hash(account['password'], password):
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            return redirect(url_for('home'))
        else:
            flash("Incorrect username/password!", "danger")
    
    return render_template('auth/login.html', title="Login")


# Register page
@app.route('/pythonlogin/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        # Validate inputs
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()

        if account:
            flash("Account already exists!", "danger")
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            flash("Invalid email address!", "danger")
        elif not re.match(r'[A-Za-z0-9]+', username):
            flash("Username must contain only characters and numbers!", "danger")
        elif not username or not password or not email:
            flash("Please fill out the form!", "danger")
        else:
            hashed_password = generate_password_hash(password)
            cursor.execute('INSERT INTO accounts (username, email, password) VALUES (%s, %s, %s)', 
                           (username, email, hashed_password))
            mysql.connection.commit()
            flash("You have successfully registered!", "success")
            return redirect(url_for('login'))

    return render_template('auth/register.html', title="Register")


# Home page (accessible after login)
@app.route('/')
def home():
    if 'loggedin' in session:
        return render_template('home/home.html', username=session['username'], title="Home")
    return redirect(url_for('login'))


# Profile page with CRUD operations
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE id = %s', (session['id'],))
        account = cursor.fetchone()

        if request.method == 'POST':
            # Edit profile (update username/email)
            new_username = request.form['username']
            new_email = request.form['email']
            current_password = request.form['current_password']
            new_password = request.form['new_password']
            confirm_password = request.form['confirm_password']

            # Update username and email
            if new_username and new_email:
                if not re.match(r'[A-Za-z0-9]+', new_username):
                    flash("Username must contain only characters and numbers!", "danger")
                elif not re.match(r'[^@]+@[^@]+\.[^@]+', new_email):
                    flash("Invalid email address!", "danger")
                else:
                    cursor.execute('UPDATE accounts SET username = %s, email = %s WHERE id = %s', 
                                   (new_username, new_email, session['id']))
                    mysql.connection.commit()
                    flash("Profile updated successfully!", "success")
                    session['username'] = new_username  # Update session username

            # Change password
            if current_password and new_password and confirm_password:
                if not check_password_hash(account['password'], current_password):
                    flash("Incorrect current password!", "danger")
                elif new_password != confirm_password:
                    flash("New passwords do not match!", "danger")
                elif len(new_password) < 8:
                    flash("Password must be at least 8 characters long!", "danger")
                else:
                    hashed_new_password = generate_password_hash(new_password)
                    cursor.execute('UPDATE accounts SET password = %s WHERE id = %s', 
                                   (hashed_new_password, session['id']))
                    mysql.connection.commit()
                    flash("Password updated successfully!", "success")

        return render_template('auth/profile.html', account=account, title="Profile")
    return redirect(url_for('login'))



# Logout route
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
