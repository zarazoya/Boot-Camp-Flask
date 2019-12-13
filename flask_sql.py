from flask import Flask,jsonify
import sqlite3 as sq


#creating Table

c.execute(""" CREATE TABLE employee (
    id integer,
    title text,
    description text,
    done text
    ) """)
conn.commit()


app = Flask(__name__)

@app.route("/getapi")
def getapi():
    conn = sq.connect("ApiDatabase.db")
    #creating database file with the name UsmanDataBase
    c = conn.cursor()
    c.execute("SELECT * FROM employee")
    data = c.fetchall()
    return jsonify({"data":data})

@app.route("/getsingleapi/<idx>",methods=['GET'])
def getsingleapi(idx):
    conn = sq.connect("ApiDatabase.db")
    #creating database file with the name UsmanDataBase
    c = conn.cursor()
    c.execute("SELECT * FROM employee WHERE id = ?",(idx,))
    data = c.fetchall()
    return jsonify({"data":data})

@app.route("/postapi/<idx>/<title>/<desc>/<done>",methods=['POST'])
def postapi(idx,title,desc,done):
    idx = idx
    title = title
    desc = desc
    done = done
    conn = sq.connect("ApiDatabase.db")
    #creating database file with the name UsmanDataBase
    c = conn.cursor()
    c.execute("INSERT INTO employee VALUES(?,?,?,?)",(idx,title,desc,done))
    conn.commit()
    return jsonify({"result":"added"})

@app.route("/putapi/<idx>/<title>/<value>",methods=['PUT'])
def putapi(idx,title,value):
    conn = sq.connect("ApiDatabase.db")
    #creating database file with the name UsmanDataBase
    c = conn.cursor()
    c.execute("UPDATE employee SET title=? where id =? ",(value,idx))
    conn.commit()
    return jsonify({"result":"updated"})

if __name__ == "__main__":
    app.run(debug=True)
