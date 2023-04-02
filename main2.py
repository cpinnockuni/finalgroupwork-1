from flask import Flask, render_template, request, redirect, url_for, session
from functools import wraps
from flask import flash
from flask import make_response


import os
import mysql.connector
from dotenv import load_dotenv


load_dotenv()

# Retrieve environment variables for database connection
host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
database = os.getenv('DB_DATABASE')

# Connect to MySQL database
cnx = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

app = Flask(__name__, static_url_path='/static')


app.secret_key = "secret_key"
app.secret_key = 'mysecretkey'

@app.route("/")
def home():

    resp = make_response(render_template("index.html"))
    resp.set_cookie("flavor", "choco", samesite="Lax")
    return resp





# Define a decorator to check if the user is logged in
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Redirect to login page if GET request
    if request.method == 'GET':
        return '''
            <form method="post">
                <p>Email: <input type="text" name="email"></p>
                <p>Password: <input type="password" name="password"></p>
                <p><input type="submit" value="Login"></p>
            </form>
        '''

    # Retrieve user credentials from request data
    email = request.form.get('email')
    password = request.form.get('password')

    # Create database connection and cursor
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()

    # Query users table for matching email and password
    query = "SELECT * FROM users WHERE email = %s AND password = %s"
    values = (email, password)
    cursor.execute(query, values)

    # Retrieve matching user from query result
    user = cursor.fetchone()

    # Close database connection and cursor
    cursor.close()
    cnx.close()

    # Check if user exists and redirect to appropriate page with flash message
    if user:
        flash('Login successful!', 'success')
        return redirect(url_for('community'))
    else:
        flash('Invalid credentials.', 'error')
        return redirect(url_for('login'))


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method=="POST":
    # Retrieve user details from request data
     username = request.form.get('username')
     email = request.form.get('email')
     password = request.form.get('password')

    # Create database connection and cursor
     cnx = mysql.connector.connect(**db_config)
     cursor = cnx.cursor()

    # Insert user details into users table
     query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
     values = (username, email, password)
     cursor.execute(query, values)

    # Commit changes and close database connection
     cnx.commit()
     cursor.close()
     cnx.close()




@app.route("/about")
def about():
    return render_template("about.html")




@app.route("/contact")
def contact():

    return render_template ("contact.html")






@app.route("/services")

def services():
   return render_template("services.html")




app.route('/community')
@login_required
def community():

    return render_template ("community.html")


@app.route("/freshergude")
def fresherguide():
    return render_template("fresherguide.html")



if __name__ == '__main__':
    app.run(debug=True)