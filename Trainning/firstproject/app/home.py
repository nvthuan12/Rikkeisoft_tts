import os
from fileinput import filename 
from flask import * 

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')   
def login():   
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def submit():

    username = request.form.get('username')

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
        return render_template('home.html',file=f.filename)   
    
@app.route('/returnjson', methods = ['GET']) 
def ReturnJSON(): 
    if(request.method == 'GET'): 
        data = { 
            "id" : 1, 
            "Name" : "helloo", 
        } 
        return jsonify(data) 
  
if __name__ == '__main__':   
    app.run(debug=True)
    