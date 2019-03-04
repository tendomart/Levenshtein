from flask import Flask, render_template
from flask import Flask ,flash,redirect , render_template ,request ,session ,abort
import os
from requests.sessions import session


app = Flask(__name__)


# The index page
@app.route("/")
def index():
    return render_template("login.html")

@app.route('/index')
def home():
    if not session.get('logged_in'):
        return render_template('index.html')
    else:
        return "Welcome User ,You're Not Yet Logged in!"
 
# The login page
@app.route("/login" , methods=['POST'])
def get_login():
     if request.form['password'] == 'password'  and request.form['username'] == 'admin':
        session['logged_in'] = True
     else:
        flash('Sorry You Provided The Wrong Password ,Try again')
        return home()
    
@app.route("/logout")
def logout():
        session['logged_in']=False
        return home()
   

@app.route("/results")
def get_results():
    return render_template('results.html')


@app.route("/do_levenshtein_search")
def do_levenshtein_search():
    pass


if __name__ == "__main__":
     app.secret_key = os.urandom(12)
     app.run(debug=True)
