from sqlalchemy.exc import SQLAlchemyError

from config import task, db
from flask import abort, jsonify, request
from models import Task


@task.route('/')
def get_tasks():
    """Get all Tasks"""
    try:
        tasks = Task.query.all()
        return jsonify([task.to_dict() for task in tasks])
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@task.route('/<id_>')
def get_task(id_):
    """Get Task by ID"""
    task = Task.query.filter_by(id_=id_).first()
    if task:
        return jsonify(task.to_dict())
    abort(404)


@task.route('/', methods=['POST'])
def create_task():
    """Create Task"""
    try:
        task_data = request.get_json()
        task = Task(**task_data)
        db.session.add(task)
        db.session.commit()
        print(task.to_dict())
        return jsonify(task.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@task.route('/<id_>', methods=['DELETE'])
def delete_task(id_):
    task = Task.query.filter_by(id_=id_).first()
    if task:
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Task Successfully Deleted'})
    abort(404)


@task.route('/<id_>', methods=['PATCH'])
def update_task(id_):
    try:
        task_data = request.get_json()
        task = Task.query.filter_by(id_=id_).first()
        if task:
            for key, value in task_data.items():
                setattr(task, key, value)
            db.session.commit()
            return jsonify(task.to_dict()), 201
        abort(404)
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
