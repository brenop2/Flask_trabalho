# actuators.py

from flask import Blueprint, jsonify, request

# Cria um objeto Blueprint
actuators = Blueprint('atuadores', __name__)

# Simulação de estado de atuadores
actuator_status = {
    'lamp01': {'state': 'off', 'location': 'Sala'},
    'fan02': {'state': 'low', 'location': 'Quarto'},
    'valve03': {'state': 'closed', 'location': 'Jardim'}
}

@actuators.route('/list')
def list_actuators():
    """Retorna a lista de todos os atuadores e seus status."""
    return jsonify({
        'status': 'success',
        'actuators': actuator_status
    })

@actuators.route('/<actuator_id>/set_state', methods=['POST'])
def set_actuator_state(actuator_id):
    """Muda o estado de um atuador específico via POST com dados JSON."""
    if actuator_id not in actuator_status:
        return jsonify({
            'status': 'error',
            'message': f'Atuador {actuator_id} não encontrado'
        }), 404

    # Espera que o corpo da requisição seja JSON com a chave 'new_state'
    data = request.get_json()
    new_state = data.get('new_state')

    if not new_state:
        return jsonify({
            'status': 'error',
            'message': 'Chave "new_state" é obrigatória no corpo da requisição.'
        }), 400

    # Atualiza o estado
    actuator_status[actuator_id]['state'] = new_state
    
    return jsonify({
        'status': 'success',
        'message': f'Estado de {actuator_id} atualizado para {new_state}',
        'current_status': actuator_status[actuator_id]
    })