from config import db
from datetime import datetime
import uuid


class Task(db.Model):
    """Task Model defines task table"""
    __tablename__ = 'task'
    id_ = db.Column(db.String(60), primary_key=True, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    is_completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id_ = str(uuid.uuid4())

    def __str__(self):
        return f'Task {self.title} - Completed: {self.is_completed}'

    def to_dict(self):
        attributes = dict()
        for column in self.__table__.columns:
            attribute_name = column.name
            attribute_value = getattr(self, attribute_name)
            attributes[attribute_name] = attribute_value
        return attributes
