import os, uuid
from flask import Flask, request, jsonify, send_from_directory
import model

app = Flask(__name__, template_folder='app', static_folder='static')
app.debug = True

app.config['UPLOAD_FOLDER'] = 'static/img'

app.secret_key = '@123'

@app.route('/')
def index():
    return jsonify({
        'message': 'Hello World'
    })

@app.route('/img/<filename>')
def serve_image(filename):
    return send_from_directory(app.static_folder, 'img/' + filename)

@app.route('/api', methods=['GET'])
def indexApi():
    return jsonify({
        'Hello': 'Success',
        'Assads': 'sadasdas'
    })

@app.route('/api/classify', methods=['POST'])
def classify():
    if 'image' in request.files:
        file = request.files['image']
        if file.filename != '' and file.filename.rsplit('.', 1)[1].lower() in ['jpg', 'png', 'jpeg']:
            print(file)
            new_filename = uuid.uuid4().hex + '.'+file.filename.rsplit('.', 1)[1].lower()
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
            print("File path:", file_path)

            # Check if the directory exists
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.makedirs(app.config['UPLOAD_FOLDER']) 
            file.save(file_path)

            classification = model.classify(new_filename)
            print(classification)

            classification['confident_score'] = float(classification['confident_score'])

            return jsonify(classification), 201
        else:
            return jsonify({
                'error' : 'File extention is not allowed'
            }), 400
    else:
        return jsonify({
            'error' : 'Image not found'
        }),404

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', port='8080', debug=True)