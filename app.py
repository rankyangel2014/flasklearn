from flask import Flask
from database import db
from application.views.first import first
from application.views.second import second

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////root/sqlite3/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.register_blueprint(first)
app.register_blueprint(second)
