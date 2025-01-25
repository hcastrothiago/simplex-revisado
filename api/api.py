from flask import Flask, request, jsonify
from simplex_revisado import simplex_revisado
import numpy as np

app = Flask(__name__)

@app.route('/simplex_revisado', methods=['POST'])
def simplex():
    data = request.json

    c = np.array(data['c'])
    A = np.array(data['A'])
    b = np.array(data['b'])
    
    resultado = simplex_revisado(c, A, b)
    return jsonify({'resultado': resultado}), 200

@app.route('/', methods=['GET'])
def index():
    return 'API do Simplex Revisado'

if __name__ == '__main__':
    app.run(debug=True)
