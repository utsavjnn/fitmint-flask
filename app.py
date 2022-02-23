from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

#flask instance
app = Flask(__name__)

# TODO: move configs to .env
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://localhost/fitmint'

#db instance
db = SQLAlchemy(app)

#initialising migrate
migrate = Migrate(app, db)

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)

@app.route('/')
def index():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug = True)
