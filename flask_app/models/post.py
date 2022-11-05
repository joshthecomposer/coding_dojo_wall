from flask import Flask, flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import post

class Post:
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        self.comments = []

    @classmethod
    def save(cls, data):
        query = "INSERT INTO posts (user_id, content) VALUES (%(user_id)s, %(content)s)"
        return connectToMySQL('coding_dojo_wall').query_db(query, data)
        
    @classmethod
    def get_all_posts(cls):
        query = "SELECT * FROM posts JOIN users ON posts.user_id = users.id ORDER BY posts.created_at DESC"
        return connectToMySQL('coding_dojo_wall').query_db(query)

    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['content'])< 1:
            flash('*Your post has no text')
            is_valid = False
        return is_valid
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM posts WHERE id = %(id)s;"
        return connectToMySQL('coding_dojo_wall').query_db(query, data)