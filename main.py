from flask import Flask, render_template, request, redirect, url_for, session
from functools import wraps
from flask import flash
from flask import make_response

app = Flask(__name__, static_url_path='/static')


app.secret_key = "secret_key"
app.secret_key = 'mysecretkey'

@app.route("/")
def home():

    resp = make_response(render_template("index.html"))
    resp.set_cookie("flavor", "choco", samesite="Lax")
    return resp




@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            # Get the username and password from the form
            username = request.form['username']
            password = request.form['password']

            # Create database connection and cursor
            conn = psycopg2.connect(
                host=os.environ['DB_HOST'],
                port=os.environ['DB_PORT'],
                dbname=os.environ['DB_NAME'],
                user=os.environ['DB_USER'],
                password=os.environ['DB_PASSWORD']
            )
            cursor = conn.cursor()

            # Execute SQL query to fetch user with matching username and password
            query = "SELECT * FROM users WHERE username=%s AND password=%s"
            cursor.execute(query, (username, password))

            # Fetch the result
            result = cursor.fetchone()

            # Close the cursor and connection to the database
            cursor.close()
            conn.close()

            if result:
                # If user exists, redirect to the home page
                return redirect(url_for('home'))
            else:
                # If no user found, show an error message
                flash("Wrong Password or Username")
                return render_template("login.html")
        
        except Exception as error:
            # Handle any errors that occur
            print(error)
            return render_template("login.html")
         
    else:
        # If request method is GET, show the login form
        return render_template ("login.html")




@app.route("/signup", methods=['GET', 'POST'])
def signup():
     if request.method == 'POST':
         
      try:

    
        # Get the username and password from the form
         username = request.form['username']
         password = request.form['password']
    

         flash("Wrong Password or Username")

      except Exception as error:
          return render_template("signup.html")
         
     else:
         return render_template ("signup.html")






@app.route("/about")
def about():
    return render_template("about.html")




@app.route("/contact")
def contact():

    return render_template ("contact.html")












@app.route("/freshergude")
def fresherguide():
    return render_template("fresherguide.html")



if __name__ == '__main__':
    app.run(debug=True)