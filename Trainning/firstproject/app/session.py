import flask
import session
from flask import Flask, session, request, json, make_response, redirect, render_template, url_for
from datetime import timedelta
app = Flask(__name__)

app.secret_key = "abc!!!"
@app.route('/')
def index():
    if 'username' in session:
        return '''<h1> ''' + f'xin chào: {session["username"]}'+''' </h1>'''+ '''<a href="/logout">Đăng xuất</a>'''
    return '''
        <h1>Bạn chưa đăng nhập</h1>
        <a href="/login">Đăng nhập</a>
    '''


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))
