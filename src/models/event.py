from src.models.user import db  # Importa db compartilhado
from datetime import datetime
import random

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    logo_url = db.Column(db.String(500))
    primary_color = db.Column(db.String(7), default='#1e3a8a')  # azul marinho padrão
    secondary_color = db.Column(db.String(7), default='#ffffff')  # branco padrão
    accent_color = db.Column(db.String(7), default='#3b82f6')  # azul claro padrão
    audio_stream_url = db.Column(db.String(500))
    access_pin = db.Column(db.String(8), unique=True, nullable=False)  # PIN de 8 dígitos
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    
    def __init__(self, **kwargs):
        super(Event, self).__init__(**kwargs)
        if not self.access_pin:
            self.access_pin = self.generate_pin()

    def generate_pin(self):
        """Gera um PIN único de 8 dígitos"""
        while True:
            pin = ''.join([str(random.randint(0, 9)) for _ in range(8)])
            # Verifica se o PIN já existe no banco
            existing = Event.query.filter_by(access_pin=pin).first()
            if not existing:
                return pin

    def __repr__(self):
        return f'<Event {self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'logo_url': self.logo_url,
            'primary_color': self.primary_color,
            'secondary_color': self.secondary_color,
            'accent_color': self.accent_color,
            'audio_stream_url': self.audio_stream_url,
            'access_pin': self.access_pin,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'is_active': self.is_active
        }

