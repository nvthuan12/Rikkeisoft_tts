from flask import Flask
app=Flask(__name__)

app.route('/hello')
def hello():
   "<p>Hello, World!</p>"

if __name__=='__main__':
    app.run(debug=True)