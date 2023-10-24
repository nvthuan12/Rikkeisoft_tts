import os
from fileinput import filename 
from flask import * 

app = Flask(__name__)

@app.route('/')
def index():
    message = "Mời bạn đăng nhập!"
    return render_template('login.html', message=message)


@app.route('/login', methods=['POST'])
def submit():
    message= "Mời nhập lại!"
    username = request.form.get('username')
    password = request.form.get('password')
    if (username==' ' or  password==' ' ):
        return render_template('login.html',message=message)
    else:
        return render_template('home.html',username=username)

# upload file
@app.route('/upload')   
def upload():   
    return render_template("upload.html")   
  
@app.route('/upload', methods = ['POST'])   
def upload_file():   
    if request.method == 'POST':   
        f = request.files['file'] 
        f.save(f.filename)   
        return render_template("home.html", name = f.filename)   
  
if __name__ == '__main__':   
    app.run(debug=True)
    