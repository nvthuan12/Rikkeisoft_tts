import mysql.connector

from flask import *
app=Flask(__name__)

# Thiết lập kết nối đến cơ sở dữ liệu MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="test"
)
# # Tạo một con trỏ để thao tác với cơ sở dữ liệu
# cursor = db.cursor()

# # Thêm một bản ghi mới vào bảng user
# insert_query = "INSERT INTO user (username, password) VALUES (%s, %s)"
# user_data = ("Chuong", "001122")  # Thay đổi giá trị này bằng thông tin người dùng thực tế

# cursor.execute(insert_query, user_data)

# # Lưu thay đổi vào cơ sở dữ liệu
# db.commit()

# # Đóng kết nối
# db.close()

@app.route('/')
def index():
    cursor = db.cursor()
    query = "SELECT * FROM user"
    cursor.execute(query)
    result = cursor.fetchall()
    return render_template('index.html',result=result)

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method=='Post':
        name_user=request.form['name_user']
        email=request.form['email']
        password=request.form['password']
        cursor=db.cursor()
        query="INSERT INTO user(name_user,email,'password') VALUES (%s,%s,%s)"
        values=(name_user,email,password)
        cursor.execute(query,values)
        db.commit()
        return redirect(url_for('index'),)
    return render_template('register.html')

if __name__=='__main__':
    app.run(debug=True)