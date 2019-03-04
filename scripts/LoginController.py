from flask import Flask
from flask import Flask ,flash,redirect , render_template ,request ,session ,abort
import os

app = Flask(__name__)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Welcome User ,You're Not Yet Logged in!"
    
@app.route('/login' , methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password'  and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('Sorry You Provided The Wrong Password ,Try again')
        return home()
    
    @app.route("/logout")
    def logout():
        session['logged_in']=False
        return home()
    
    if __name__== "__main__":
        app.secret_key = os.urandom(12)
        app.run(host='0.0.0.0',port=4000,debug=True, )
    
    