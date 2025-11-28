# Libraries
from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import re

app = Flask(__name__)
app.secret_key = 'supersecretkey'

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def is_valid_name(name):
    return not bool(re.search(r'\d', name))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE id = ?", (session['user_id'],))
    user = c.fetchone()
    conn.close()

    return render_template('profile.html', user=user)

# Route to handle name change
@app.route('/change_name', methods=['POST'])
def change_name():
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    if not is_valid_name(first_name) or not is_valid_name(last_name):
        flash('Names cannot contain numbers.', 'danger')
    else:
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("UPDATE users SET first_name = ?, last_name = ? WHERE id = ?",
                  (first_name, last_name, session['user_id']))
        conn.commit()
        conn.close()
        flash('Name updated successfully!', 'success')

    return redirect(url_for('profile'))

# Route to handle password change
@app.route('/change_password', methods=['POST'])
def change_password():
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    old_password = request.form['old_password']
    new_password = request.form['new_password']
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT password FROM users WHERE id = ?", (session['user_id'],))
    user = c.fetchone()
    if user and check_password_hash(user[0], old_password):
        hashed_password = generate_password_hash(new_password)
        c.execute("UPDATE users SET password = ? WHERE id = ?",
                  (hashed_password, session['user_id']))
        conn.commit()
        conn.close()
        flash('Password updated successfully!', 'success')
    else:
        flash('Old password is incorrect.', 'danger')

    return redirect(url_for('profile'))

# Route to handle email change
@app.route('/change_email', methods=['POST'])
def change_email():
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    new_email = request.form['new_email']
    if not is_valid_email(new_email):
        flash('Invalid email address.', 'danger')
    else:
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, session['user_id']))
        conn.commit()
        conn.close()
        flash('Email updated successfully!', 'success')

    return redirect(url_for('profile.html'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        c.execute("SELECT * FROM users WHERE email=?", (email,))
        user = c.fetchone()
        if user and check_password_hash(user[5], password):
            session['user_id'] = user[0]
            session['username'] = user[3]
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password.', 'danger')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_id = str(uuid.uuid4())
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Passwords do not match.', 'danger')
            return redirect(url_for('register'))

        if not is_valid_email(email):
            flash('Invalid email address.', 'danger')
            return redirect(url_for('register'))

        if not is_valid_name(first_name) or not is_valid_name(last_name):
            flash('Names cannot contain numbers.', 'danger')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password)

        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        c.execute("SELECT * FROM users WHERE email=?", (email,))
        if c.fetchone():
            flash('This email is already registered.', 'danger')
            return redirect(url_for('register'))

        c.execute("INSERT INTO users (id, first_name, last_name, username, email, password) VALUES (?, ?, ?, ?, ?, ?)",
                  (user_id, first_name, last_name, username, email, hashed_password))
        conn.commit()
        conn.close()

        flash('Registration successful!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/privacyandcookies')
def privacy():
    return render_template('policies.html')

@app.route('/forecast')
def forecast():
    return render_template('forecast.html')

@app.route('/airquality')
def airquality():
    return render_template('air.html')

@app.route('/health')
def health():
    return render_template('health.html')

@app.route('/riskassessment')
def riskassessment():
    return render_template('risk.html')

@app.route('/contact-us')
def contact():
    return render_template('contact.html')

@app.route('/access')
def access():
    return render_template('access.html')

if __name__ == "__main__":
    app.run(debug=True)
