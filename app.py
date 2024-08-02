
from flask import Flask, render_template, request, redirect, url_for
import psycopg2  # Import the PostgreSQL library
 
app = Flask(__name__, template_folder='Templates')
 
# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="root",
    host="localhost",
    port="5433"
)
cursor = conn.cursor()
 
@app.route('/')
def login():
    return render_template("login.html")
 
@app.route('/login_validation', methods=['POST'])
def login_validation():
    username = request.form.get('Uname')
    password = request.form.get('Pass')
    # Get valid users with the entered user name and password
    cursor.execute("SELECT * FROM login_table WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchall()
    if len(user) > 0:
        return redirect(url_for('home'))
    else:
        return render_template("login.html")
 
@app.route('/home')
def home():
    return render_template("home.html")
 
@app.route('/logout')
def logout():
    return redirect(url_for('login'))
 
@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.form.get('Uname')
    email = request.form.get('Email')
    password = request.form.get('Pass')
    cursor.execute(
        "INSERT INTO login_table (username, email, password) VALUES (%s, %s, %s)",
        (username, email, password)
    )
    conn.commit()
    return render_template('login.html')
 
@app.route('/register')
def register():
    return render_template("register.html")
 
if __name__ == '__main__':
    app.run(debug=True)

 