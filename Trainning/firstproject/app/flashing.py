from flask import*
app=Flask(__name__)

app.secret_key="abc!"

@app.route('/')
def index():
    if 'username' in session:
       username=session['username']
       return render_template('index.html',username=username)
    else:
        return render_template('login.html')

@app.route('/login',methods=['GET','POST'])
def login():
    error=None
    if request.method=='POST':
        username=request.form.get('username')
        password = request.form.get('password')
        if username != 'admin' or password != 'admin':
            error ='nhập sai tài khoản hoặc mật khẩu!'
        else: 
            session['username']=request.form['username']
            flash("Đăng nhập thành công!")
            return redirect(url_for('index'))
    return render_template('login.html',error=error)         

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))       
    