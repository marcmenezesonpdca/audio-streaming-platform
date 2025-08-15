from flask import Blueprint, request, jsonify
from src.models.user import db  # Importa db do modelo user principal
from src.models.event import Event
from src.models.participant import Participant

event_bp = Blueprint('event', __name__)

@event_bp.route('/events', methods=['GET'])
def get_events():
    """Lista todos os eventos"""
    events = Event.query.filter_by(is_active=True).all()
    return jsonify([event.to_dict() for event in events])

@event_bp.route('/events', methods=['POST'])
def create_event():
    """Cria um novo evento"""
    data = request.get_json()
    
    if not data or not data.get('name'):
        return jsonify({'error': 'Nome do evento é obrigatório'}), 400
    
    event = Event(
        name=data['name'],
        description=data.get('description', ''),
        logo_url=data.get('logo_url', ''),
        primary_color=data.get('primary_color', '#1e3a8a'),
        secondary_color=data.get('secondary_color', '#ffffff'),
        accent_color=data.get('accent_color', '#3b82f6'),
        audio_stream_url=data.get('audio_stream_url', '')
    )
    
    db.session.add(event)
    db.session.commit()
    
    return jsonify(event.to_dict()), 201

@event_bp.route('/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    """Obtém um evento específico"""
    event = Event.query.get_or_404(event_id)
    return jsonify(event.to_dict())

@event_bp.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    """Atualiza um evento"""
    event = Event.query.get_or_404(event_id)
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'Dados não fornecidos'}), 400
    
    # Atualiza os campos fornecidos
    for field in ['name', 'description', 'logo_url', 'primary_color', 
                  'secondary_color', 'accent_color', 'audio_stream_url']:
        if field in data:
            setattr(event, field, data[field])
    
    db.session.commit()
    return jsonify(event.to_dict())

@event_bp.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    """Desativa um evento (soft delete)"""
    event = Event.query.get_or_404(event_id)
    event.is_active = False
    db.session.commit()
    return jsonify({'message': 'Evento desativado com sucesso'})

@event_bp.route('/events/<int:event_id>/pin', methods=['GET'])
def get_event_pin(event_id):
    """Obtém o PIN do evento"""
    event = Event.query.get_or_404(event_id)
    return jsonify({
        'pin': event.access_pin,
        'event_name': event.name
    })

@event_bp.route('/events/access', methods=['POST'])
def access_event_by_pin():
    """Acessa evento pelo PIN"""
    data = request.get_json()
    
    if not data or not data.get('pin'):
        return jsonify({'error': 'PIN é obrigatório'}), 400
    
    pin = data['pin'].strip()
    
    # Valida se o PIN tem 8 dígitos
    if len(pin) != 8 or not pin.isdigit():
        return jsonify({'error': 'PIN deve conter exatamente 8 dígitos'}), 400
    
    event = Event.query.filter_by(access_pin=pin, is_active=True).first()
    
    if not event:
        return jsonify({'error': 'PIN inválido ou evento não encontrado'}), 404
    
    return jsonify({
        'success': True,
        'event': event.to_dict(),
        'message': 'Acesso autorizado'
    })

@event_bp.route('/events/pin/<pin>/register', methods=['POST'])
def register_participant_by_pin(pin):
    """Registra um participante no evento usando PIN"""
    event = Event.query.filter_by(access_pin=pin, is_active=True).first_or_404()
    data = request.get_json()
    
    if not data or not data.get('name') or not data.get('email'):
        return jsonify({'error': 'Nome e email são obrigatórios'}), 400
    
    # Verifica se já está registrado
    existing = Participant.query.filter_by(
        email=data['email'], 
        event_id=event.id
    ).first()
    
    if existing:
        return jsonify({'message': 'Participante já registrado', 'participant': existing.to_dict()})
    
    participant = Participant(
        name=data['name'],
        email=data['email'],
        event_id=event.id
    )
    
    db.session.add(participant)
    db.session.commit()
    
    return jsonify({
        'message': 'Participante registrado com sucesso',
        'participant': participant.to_dict(),
        'event': event.to_dict()
    }), 201

@event_bp.route('/events/<int:event_id>/participants', methods=['GET'])
def get_event_participants(event_id):
    """Lista participantes de um evento"""
    event = Event.query.get_or_404(event_id)
    participants = Participant.query.filter_by(event_id=event_id).all()
    return jsonify([participant.to_dict() for participant in participants])

