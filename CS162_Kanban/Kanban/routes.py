from flask import Flask, url_for, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy
from Kanban import db, app

# Create Doing Table
class Doing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.String(2000))

# Create To_do Table
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.String(2000))

# Create Done Table
class Done(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.String(2000))

# Create Home Page
@app.route('/')
def index():
    doings = Doing.query.all()
    todos=Todo.query.all()
    dones=Done.query.all()
    return render_template('index.html', doings=doings, todos=todos, dones=dones)

# Add an event
@app.route('/add1',methods=['POST','GET'])
def add1():
    doing = Doing(title=request.form['title1'], description=request.form['description1'])
    db.session.add(doing)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/add2',methods=['POST','GET'])
def add2():
    todo = Todo(title=request.form['title2'], description=request.form['description2'])
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/add3',methods=['POST','GET'])
def add3():
    done = Done(title=request.form['title3'], description=request.form['description3'])
    db.session.add(done)
    db.session.commit()
    return redirect(url_for('index'))

# Commands for an existing event
@app.route('/change1',methods=['POST','GET'])
def change1():
    doing=request.form['doing']
    if doing=='DONE':
        record = Doing.query.get(request.form['id'])
        done=Done(title=request.form['title'],description=request.form['description'])
        db.session.add(done)
        db.session.delete(record)
        db.session.commit()

    elif doing == 'TODO':
        record = Doing.query.get(request.form['id'])
        todo = Todo(title=request.form['title'], description=request.form['description'])
        db.session.add(todo)
        db.session.delete(record)
        db.session.commit()

    if doing == 'DELETE':
        record=Doing.query.get(request.form['id'])
        db.session.delete(record)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/change2',methods=['POST','GET'])
def change2():
    todo=request.form['todo']
    if todo=='DONE':
        record = Todo.query.get(request.form['id'])
        done=Done(title=request.form['title'],description=request.form['description'])
        db.session.add(done)
        db.session.delete(record)
        db.session.commit()

    elif todo == 'DOING':
        record = Todo.query.get(request.form['id'])
        doing = Doing(title=request.form['title'], description=request.form['description'])
        db.session.add(doing)
        db.session.delete(record)
        db.session.commit()

    if todo == 'DELETE':
        record=Todo.query.get(request.form['id'])
        db.session.delete(record)
        db.session.commit()

    return redirect(url_for('index'))


@app.route('/change3', methods=['POST','GET'])
def change3():
    done=request.form['done']
    if done == 'TODO':
        record = Done.query.get(request.form['id'])
        todo = Todo(title=request.form['title'], description=request.form['description'])
        db.session.add(todo)
        db.session.delete(record)
        db.session.commit()

    elif done == 'DOING':
        record = Done.query.get(request.form['id'])
        doing = Doing(title=request.form['title'], description=request.form['description'])
        db.session.add(doing)
        db.session.delete(record)
        db.session.commit()

    if done == 'DELETE':
        record = Done.query.get(request.form['id'])
        db.session.delete(record)
        db.session.commit()

    return redirect(url_for('index'))

