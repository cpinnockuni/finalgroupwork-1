from flask import Flask, render_template, request, redirect, url_for, session
from functools import wraps
from flask import flash


app = Flask(__name__, static_url_path='/static')


app.secret_key = "secret_key"
app.secret_key = 'mysecretkey'

@app.route("/")
def home():



    return render_template ("index.html")






# Define a decorator to check if the user is logged in
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route("/login", methods=['GET', 'POST'])
def login():
     if request.method == 'POST':
         
      try:

    
        # Get the username and password from the form
         username = request.form['username']
         password = request.form['password']
    

         flash("Wrong Password or Username")

      except Exception as error:
          return render_template("login.html")
         
     else:
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
    pass 




@app.route("/contact")
def contact():

    return render_template ("contact.html")






@app.route("/services/community")
@login_required
def community():
    pass 





@app.route("/services/freshergude")
def fresherguide():
    pass



if __name__ == '__main__':
    app.run(debug=True, port=5000)