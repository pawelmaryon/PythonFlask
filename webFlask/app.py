from flask import Flask, render_template, request, url_for, redirect, abort, Response
import sqlite3 as sql



app = Flask(__name__)

def musicDBCon():
  conn = sql.connect("PythonFlask/webFlask/c8MyMusic.db")
  conn.row_factory = sql.Row
  return conn


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title="Index")

@app.route('/about')
def about():
    return render_template("about.html", title="About")

@app.route('/contact')
def contact():
    return render_template("contact.html", title="Contact")

@app.route('/songs')
def songs():
    conn = musicDBCon()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM songs')

    getSongs = cursor.fetchall()

    return render_template("songs.html", title="Songs", allSongs = getSongs)

@app.route('/addsongs')
def addsongs():
    return render_template("addsongs.html", title="Add Songs")


if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0", port=8900)