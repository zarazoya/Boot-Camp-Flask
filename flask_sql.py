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


if __name__ == "__main__":
    app.run(debug=True)
