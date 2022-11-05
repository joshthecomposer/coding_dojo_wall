from flask_app import app
from flask_app.controllers import main_controller, posts, users, comments

if __name__ == '__main__':
    app.run(debug=True)