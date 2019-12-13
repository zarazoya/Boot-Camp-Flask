from flask import Flask,jsonify
import sqlite3 as sq

conn = sq.connect("ApiDatabase.db")
c = conn.cursor()

#creating Table

c.execute(""" CREATE TODO LIST TABLE (
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
    #creating database file with the name ZoyaDataBase
    c = conn.cursor()
    c.execute("SELECT * FROM employee")
    data = c.fetchall()
    return jsonify({"data":data})


if __name__ == "__main__":
    app.run(debug=True)
