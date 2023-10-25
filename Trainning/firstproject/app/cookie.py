from flask import Flask, render_template, request, make_response,abort,url_for,redirect
app = Flask(__name__)

@app.route('/')
def index():
    # đọc giá trị cookie từ yêu cầu
    user_cookie= request.cookies.get('user_cookie')
    if user_cookie:
        return f"hello {user_cookie}"
    else:
        response=make_response("welcome! ")    
        response.set_cookie('user_cookie',"thuan", path='/', max_age=5)

        return response
    
@app.route('/home')
def home():
    return redirect(url_for('login'))

# @app.route('/login')
# def login():
#     abort(401)
#     this_is_never_executed()

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
    
