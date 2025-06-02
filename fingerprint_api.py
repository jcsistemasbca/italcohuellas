from flask import Flask, request, jsonify
from flask_cors import CORS
from sourceafis import FingerprintTemplate, FingerprintMatcher
import base64

app = Flask(__name__)
CORS(app)

@app.route('/compare', methods=['POST'])
def compare():
    data = request.get_json()
    first = data.get('firstFeatureSet')
    second = data.get('secondFeatureSet')
    if not first or not second:
        return jsonify({'error': 'Faltan datos de huellas'}), 400

    try:
        probe_bytes = base64.b64decode(first)
        candidate_bytes = base64.b64decode(second)
        probe = FingerprintTemplate(probe_bytes)
        candidate = FingerprintTemplate(candidate_bytes)
        matcher = FingerprintMatcher(probe)
        score = matcher.match(candidate)
        return jsonify({'success': True, 'score': score})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5001)