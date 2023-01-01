from flask import Flask, request, flash, url_for, redirect, render_template, json
from app.database import userLogin
from app import app, db

@app.route('/', methods=['GET', 'POST'])
def login():
    db.create_all()
    if request.method == 'POST':
        user_name = request.form.get('uname') 
        password = request.form.get('psw')
        if user_name == 'Admin':
            return redirect(url_for('view_progress'))
        else:
            return render_template('')
    return render_template('login.html')


@app.route('/admin', methods=['GET', 'POST'])
def view_progress():
    if request.method == 'POST':
        return redirect(url_for('add_mem'))
    data=userLogin.query.all()
    return render_template('2nd.html',data=data)

@app.route('/addmember',methods=['GET','POST'])
def add_mem():
    if request.method=='POST':
        user_name= request.form.get('uname')
        password = request.form.get('psw')
        user = userLogin(user_name,password)
        db.session.add(user)
        db.session.commit()  
        flash('Record was successfully added')
        return render_template('3rd.html')
    return render_template('3rd.html')
