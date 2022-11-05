from flask import redirect, request, session, flash
from flask_app import app
from flask_app.controllers import main_controller, posts
from flask_app.models import user
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/register', methods=['POST'])
def register():
    check_email = {
        'email' : request.form['email']
    }
    user_exists = user.User.email_lookup(check_email)
    if user_exists:
        flash('Email already registered')
        session['form_tried'] = 'register'
        return redirect('/')
    is_valid = user.User.validate(request.form)
    if is_valid == True:
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pw_hash
        }
        
        user_id = user.User.save(data)
        session['user_id'] = user_id
        return redirect('/wall')
    session['form_tried'] = 'register'
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    data = {
        'email': request.form['email']
    }
    user_exists = user.User.email_lookup(data)
    if not user_exists:
        flash('Email/Password invalid')
        session['form_tried'] = 'login'
        return redirect('/')
    if not bcrypt.check_password_hash(user_exists[0]['password'], request.form['password']):
        flash('Email/Password invalid')
        session['form_tried'] = 'login'
        return redirect('/')
    session['user_id'] = user_exists[0]['id']
    return redirect('/wall')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')