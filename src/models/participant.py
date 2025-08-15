from src.models.user import db  # Importa db compartilhado
from datetime import datetime

class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    registered_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relacionamento com Event
    event = db.relationship('Event', backref=db.backref('participants', lazy=True))

    def __repr__(self):
        return f'<Participant {self.name} - Event {self.event_id}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'event_id': self.event_id,
            'registered_at': self.registered_at.isoformat() if self.registered_at else None
        }

