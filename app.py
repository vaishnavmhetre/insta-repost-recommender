from flask import Flask
from flask_cors import CORS
from DB.DBHelper import DBHelper

# configure our database

DATABASE = {
    'name': 'storage/storage.db',
    'engine': 'peewee.SqliteDatabase',
}

INSTAGRAM_CONFIG = {
    'username': 'fashionstreetig',
    'password': "mahajan@123"
}

MAX_CLIENTS = 150

DEBUG = True
SECRET_KEY = 'ssshhhh'
MAX_RECOMMENDATIONS = 10

app = Flask(__name__)
app.config.from_object(__name__)
CORS(app)


@app.route('/posts', methods=['GET'])
def showPostsHandle():
    from Controller.PostsController import showPosts
    return showPosts()


@app.route('/posts/<postId>/ignore', methods=['POST'])
def markAsIgnoredHandle(postId):
    from Controller.PostsController import markAsIgnored
    return markAsIgnored(postId)


@app.route('/posts/<postId>/posted', methods=['POST'])
def markAsPostedHandle(postId):
    from Controller.PostsController import markAsPosted
    return markAsPosted(postId)


# instantiate the db wrapper


db = DBHelper(app).db

if __name__ == '__main__':
    # db.create_tables([Post, ClientUser], fail_silently=True)

    app.run()
