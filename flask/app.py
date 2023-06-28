from flask import Flask,render_template,request
import mysql.connector
user_dict={'admin':'admin','user':'5678'}
conn = mysql.connector.connect(host='localhost',user='root',password='',database='manutd')
mycursor=conn.cursor()
#create a flask application
app = Flask(__name__)

#Define the route 

@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/employee')
def employee():
    return render_template('emp.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/admin',methods=['POST'])
def home():
    uname=request.form['username']
    pwd=request.form['password']

    if uname not in user_dict:
        return render_template('login.html',msg='Invalid User')
    elif user_dict[uname] != pwd:
        return render_template('login.html',msg='Invalid Password')
    else:
        return render_template('admin.html')

@app.route('/list')
def view():
    query="SELECT * FROM players"
    mycursor.execute(query)
    data=mycursor.fetchall()
    return render_template('list.html',sqldata=data)

@app.route('/search')
def searchpage():
    return render_template('search.html')


@app.route('/searchresult',methods=['POST'])
def search():
    pno = request.form['jno']
    query="SELECT * FROM players WHERE jno="+pno
    mycursor.execute(query)
    data=mycursor.fetchall()
    return render_template('list.html',sqldata=data)
    
@app.route('/add')
def add():
    return render_template('player.html')

@app.route('/read',methods=['POST'])
def read():
    pno = request.form['jno']
    name = request.form['pname']
    age= request.form['page']
    country = request.form['pcountry']
    query = "INSERT INTO players(jno, name, age, country) VALUES (%s,%s,%s,%s)"
    data = (pno, name, age, country)
    mycursor.execute(query,data)
    conn.commit()
    return render_template('player.html',msgdata='Player has been added to the List')

#Run the flask app
if __name__=='__main__':
    app.run(port=5001,debug = True)