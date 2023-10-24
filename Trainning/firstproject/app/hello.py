# from flask import Flask, url_for
# from markupsafe import escape
# app = Flask(__name__)

# @app.route("/")
# def home1():
#     return "Wellcome home1"

# @app.route("/home2/")
# def home2():
#     return "HOME 2"

# @app.route("/user/<username>")
# def profile(username):
#     return f'{username}\'s profile'

# with app.test_request_context():
#     print(url_for('home1'))
#     print(url_for('home2'))
#     print(url_for('home2', next="/"))
#     print(url_for('profile', username='John Doe'))

# if __name__ == '__main__':
#     app.run(debug=True)
