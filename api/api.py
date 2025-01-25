from flask import Flask, request, jsonify
from api.simplex_revisado import simplex_revisado
import numpy as np

app = Flask(__name__)

@app.route('/simplex_revisado', methods=['POST'])
def simplex():
    data = request.json
    c = np.array(data.get('c'))
    A = np.array(data.get('A'))
    b = np.array(data.get('b'))
    
    resultado = simplex_revisado(c, A, b)
    return jsonify({'resultado': resultado}), 200

if __name__ == '__main__':
    app.run(debug=True)
