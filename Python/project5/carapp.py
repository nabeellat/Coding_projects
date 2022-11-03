#Nabeel Latifi
#Project 4 
"""web application"""
from flask import Flask, url_for, request, redirect, render_template
import sqlite3
import datetime
import time

app = Flask(__name__)
def get_db():#Code provided by professor Dumas
    """Open a connection to the database and return the connection object"""
    con = sqlite3.connect("cars.sqlite3")
    con.row_factory = sqlite3.Row # return dict-like rows
    return con

login_render = """<!DOCTYPE html>
<html>
<div class="compose-form">
<form action="/login">
  <label for="username">username:</label>
  <input type="text" id="username" name="username"><br><br>
  <label for="password">Password:</label>
  <input type="text" id="password" name="password"><br><br>
  <input type="submit" value="Submit">
</form>"""

home_render = """
<!DOCTYPE html>
<html>
<body>

<table>
<th></th>
<tr>
<td>{car name}</td>
<td>{car year}</td>
</tr>
</table>

</body>
</html>

"""



@app.route('/login', methods=['GET', 'POST'])
def login():#refer to citation
    """login check"""
    error = None
    con = sqlite3.connect("car.sqlite3")
    if request.method == 'POST':
        if request.form['username'] != con.execute("SELECT usernamme FROM userinfo WHERE {}=username;".format(request.form['username'])) or request.form['password'] != con.execute("SELECT usernamme FROM userinfo WHERE {}=username;".format(request.forn['username'])):
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('/home'))
    return render_template(login_render, error=error)
@app.route("/")
@app.route("/createnew")
def createnewaccount():
    "create new account url"
    return login_render
@app.route("/")
@app.route("/home")
def home_page():
    """home page"""
    con = sqlite3.connect("car.sqlite3")

    

@app.route("/")
@app.route("/buy")
def sale():
    "sale "
    return "sale"
if __name__=="__main__":
    app.run()
