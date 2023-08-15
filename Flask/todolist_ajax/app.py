from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa
import json


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(100))
    complete = sa.Column(sa.Boolean)

    def serialize(self):
        return {"id": self.id, "title": self.title, "complete": self.complete}


with app.app_context():
    db.create_all()


@app.get("/")
def home():
    return render_template("base.html")


@app.get("/api/")
def api():
    todo_list = db.session.query(Todo).all()
    return jsonify({"data": [x.serialize() for x in todo_list]})


@app.post("/api/add/")
def add():
    data = request.data.decode("utf-8")
    data = json.loads(data)
    title = data.get("title", "")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return jsonify(new_todo.serialize())


@app.get("/api/update/<int:todo_id>/")
def update(todo_id):
    todo = db.session.query(Todo).filter(Todo.id==todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return jsonify(todo.serialize())


@app.get("/api/delete/<int:todo_id>/")
def delete(todo_id):
    todo = db.session.query(Todo).filter(Todo.id==todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return jsonify({"todo_id": todo_id})


if __name__ == "__main__":
    app.run()
    