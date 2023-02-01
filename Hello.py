from flask import Flask , render_template , request , redirect, url_for
import psycopg2

conn = psycopg2.connect(
            database = "studentdb",
            user = "postgres",
            password = "password",
            host = "localhost",
            port = "5432")

app = Flask(__name__)

@app.route("/")
def showData():
    with conn :
        cur = conn.cursor()
        cur.execute("SELECT * FROM student")
        rows = cur.fetchall()

    return render_template("index.html",datas=rows)

@app.route("/student")
def showForm():
    return render_template("addstudent.html")

@app.route("/delete/<string:id_data>",methods=['GET'])
def delete(id_data):
    with conn :
        cur = conn.cursor()
        cur.execute("DELETE from student where id= %s",(id_data))
        conn.commit()
    return redirect(url_for('showData'))

@app.route("/insert",methods=['POST'])
def insert():
    if request.method=="POST":
        fname = request.form['fname']
        lname = request.form['lname']
        phone = request.form['phone']
        with conn:
            cur = conn.cursor()
            sql = "INSERT INTO student(fname,lname,phone) VALUES (%s,%s,%s)"
            cur.execute(sql,(fname,lname,phone))
            conn.commit()
        return redirect(url_for('showData'))

@app.route("/update",methods=['POST'])
def update():
    if request.method=="POST":
        fname = request.form['fname']
        lname = request.form['lname']
        phone = request.form['phone']
        id = request.form['id']
        with conn:
            cur = conn.cursor()
            sql = "UPDATE student SET fname = %s , lname = %s , phone = %s WHERE id = %s"
            cur.execute(sql,(fname,lname,phone,id))
            conn.commit()
        return redirect(url_for('showData'))