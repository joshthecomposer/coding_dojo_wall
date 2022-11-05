from flask import Flask, flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import post

class Comment:
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.post_id = data['post_id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO comments (post_id, user_id, content) VALUES (%(post_id)s, %(user_id)s, %(content)s)"
        return connectToMySQL('coding_dojo_wall').query_db(query, data)
    
    @classmethod
    def get_all_comments(cls):
        query = "SELECT * FROM comments LEFT JOIN posts ON posts.id = comments.post_id LEFT JOIN users ON users.id = comments.user_id;"
        result = connectToMySQL('coding_dojo_wall').query_db(query)
        print(result)
        return result