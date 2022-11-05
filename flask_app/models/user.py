from flask import Flask, flash
import re
from flask_app.config.mysqlconnection import connectToMySQL

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{4,}$")

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL('coding_dojo_wall').query_db(query, data)
    
    @classmethod
    def get_one_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        return connectToMySQL('coding_dojo_wall').query_db(query, data)
    
    @staticmethod
    def email_lookup(data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        return connectToMySQL('coding_dojo_wall').query_db(query, data)
    
    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['first_name']) < 2:
            flash('First name must be at least 2 characters.')
            is_valid = False
        if len(data['last_name']) < 2:
            flash('Last name must be at least 2 characters.')
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash('Invalid email format')
            is_valid = False
        if data['p_confirm'] != data['password']:
            flash('Password input did not match')
            is_valid = False
        if len(data['password']) < 4:
            flash('Password must be at least 4 characters')
            is_valid = False
        if len(data['password']) >= 4:
            if not PASSWORD_REGEX.match(data['password']):
                flash('Password must contain at least one number, one letter, and one special character')
                is_valid = False
        return is_valid