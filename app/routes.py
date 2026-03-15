from flask import Blueprint, jsonify, request
from app import db
from app.models import Task

# Blueprint = gruppo di routes con prefisso /tasks
tasks_bp = Blueprint("tasks", __name__, url_prefix="/tasks")


# GET /tasks → restituisce tutte le task
@tasks_bp.route("/", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([t.to_dict() for t in tasks]), 200


# GET /tasks/<id> → restituisce una singola task
@tasks_bp.route("/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = Task.query.get_or_404(task_id)
    return jsonify(task.to_dict()), 200


# POST /tasks → crea una nuova task
@tasks_bp.route("/", methods=["POST"])
def create_task():
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"error": "title is required"}), 400

    task = Task(
        title=data["title"],
        description=data.get("description", ""),
        done=data.get("done", False)
    )
    db.session.add(task)
    db.session.commit()
    return jsonify(task.to_dict()), 201


# PUT /tasks/<id> → modifica una task esistente
@tasks_bp.route("/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.get_json()

    if "title"       in data: task.title       = data["title"]
    if "description" in data: task.description = data["description"]
    if "done"        in data: task.done        = data["done"]

    db.session.commit()
    return jsonify(task.to_dict()), 200


# DELETE /tasks/<id> → elimina una task
@tasks_bp.route("/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "task deleted"}), 200