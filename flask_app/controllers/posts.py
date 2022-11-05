from flask import render_template, redirect, session, flash, request
from flask_app import app
from flask_app.controllers import main_controller, users
from flask_app.models import user, post, comment

@app.route('/wall')
def wall():
    if 'user_id' not in session:
        session['form_tried'] = 'wall'
        flash('SIGN IN FIRST YOU DINGUS')
        return redirect('/')
    data = {
        'id' : session['user_id']
    }
    one_user = user.User.get_one_user(data)
    all_posts = post.Post.get_all_posts()
    all_comments = comment.Comment.get_all_comments()
    return render_template('wall.html', one_user = one_user[0], all_posts = all_posts, all_comments = all_comments)

@app.route('/create_post', methods = ['POST'])
def create_post():
    is_valid = post.Post.validate(request.form)
    if is_valid == False:
        return redirect('/wall')
    data = {
        'user_id' : session['user_id'],
        'content' : request.form['content']
    }
    post.Post.save(data)
    return redirect('/wall')

@app.route('/delete', methods = ['POST'])
def delete():
    data = {
        'id' : request.form['id']
        }
    post.Post.delete(data)
    return redirect('/wall')