from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =environ.get('DATABASE_URL') or 'sqlite:///app.sqlite'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description =db.Column(db.String)



@app.route('/')
def index():
    return render_template('index.html')

    
@app.route('/tasks')
def tasks():
    tasks=db.session.query(Task)
    data=[]
    for task in tasks:
        item ={
            "id":task.id,
            "description":task.description
        }
        data.append(item)
if __name__=='__main__':
    app.run(debug=True)