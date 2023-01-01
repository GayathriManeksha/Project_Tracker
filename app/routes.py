from flask import Flask, request, flash, url_for, redirect, render_template ,json

from app import app,conn

def read():
	curr = conn.cursor()

	# EXECUTE THE SQL QUERY
	curr.execute("SELECT * FROM students;")

	# FETCH ALL THE ROWS FROM THE CURSOR
	data = curr.fetchall()

	# PRINT THE RECORDS
	for row in data:
		print(row)

@app.route('/',methods=['GET','POST'])
def login():
    if request.method=='POST':
        return redirect(url_for('view_progress'))
    return render_template('login.html')

@app.route('/admin',methods=['GET','POST'])
def view_progress():
    return render_template('2nd.html')