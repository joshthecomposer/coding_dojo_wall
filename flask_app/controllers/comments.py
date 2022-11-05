from flask import render_template, redirect, session, flash, request
from flask_app import app
from flask_app.controllers import main_controller, users
from flask_app.models import user, post, comment

@app.route('/comment', methods=['POST'])
def _comment():
    data = {
        'post_id' : request.form['post_id'],
        'user_id' : session['user_id'],
        'content' : request.form['content']
    }
    comment.Comment.save(data)
    return redirect('/wall')