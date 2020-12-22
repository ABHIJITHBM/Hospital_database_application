from flask import Flask,render_template,request,redirect
from flask_mysqldb import MySQL
app=Flask(__name__)

#configuration
app.config ['MYSQL_HOST'] ='localhost'
app.config ['MYSQL_USER'] = 'abhisql'
app.config ['MYSQL_PASSWORD'] = '123456789'
app.config ['MYSQL_DB'] = 'working_app'
mysql = MySQL(app)
@app.route('/',methods=['GET','POST'])
def index():
    print(request.method)
    if request.method=='POST':
        userDetails=request.form
        Departmentcode=userDetails['Departmentcode']
        Departmentname=userDetails['Departmentname']
        Floorno=userDetails['Floorno']
        Doctorsavailable=userDetails['Doctorsavailable']
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO Department(Department_code, Department_Name,Floor_number,Doctors_available) VALUES(%s,%s,%s,%s)",(Departmentcode, Departmentname,Floorno,Doctorsavailable))
        mysql.connection.commit()
        cur.close()
        return redirect('/users')
    return render_template('index.html')
@app.route('/users')
def Department():
    if request.method == 'GET':
        cur=mysql.connection.cursor()
        result=cur.execute("SELECT * FROM Department")
        if result>0:
            userDetails=cur.fetchall()
            return render_template('users.html',userDetails=userDetails)
if __name__=='__main__':
    app.run(debug=True)