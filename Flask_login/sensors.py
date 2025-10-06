# sensors.py

from flask import Blueprint, jsonify, request

# Cria um objeto Blueprint
# O primeiro argumento é o nome do blueprint ('sensores')
# O segundo argumento é o nome do módulo (__name__)
sensors = Blueprint('sensores', __name__)

# Simulação de dados de sensores
sensor_data = {
    'temp01': {'value': 25.5, 'unit': '°C', 'location': 'Sala'},
    'umid02': {'value': 60, 'unit': '%', 'location': 'Cozinha'},
    'pres03': {'value': 1012, 'unit': 'hPa', 'location': 'Exterior'}
}

@sensors.route('/list')
def list_sensors():
    """Retorna a lista de todos os sensores."""
    # Usando jsonify para retornar dados JSON, útil para APIs
    return jsonify({
        'status': 'success',
        'sensors': list(sensor_data.keys())
    })

@sensors.route('/<sensor_id>')
def get_sensor_data(sensor_id):
    """Retorna os dados de um sensor específico."""
    if sensor_id in sensor_data:
        return jsonify({
            'status': 'success',
            'data': sensor_data[sensor_id]
        })
    else:
        # Retorna uma resposta de erro com o código HTTP 404
        return jsonify({
            'status': 'error',
            'message': f'Sensor {sensor_id} não encontrado'
        }), 404