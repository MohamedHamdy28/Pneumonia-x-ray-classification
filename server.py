from flask import Flask, request, render_template, send_from_directory
import os, uuid
import model
import json

app = Flask(__name__)



@app.route('/')
def index():
    return send_from_directory('client/build', 'index.html')


@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/build', path)


@app.route('/upload', methods=['POST'])
def upload_file():
    
    if 'file' not in request.files:
        return json.dumps({'error': 'No file part in the request'}), 400

    file = request.files['file']


    if file.filename == '':
        return 'No selected file', 400

    allowed_extensions = ['.jpeg', '.png']

    file_extension = str(os.path.splitext(file.filename)[1])
    print(file_extension)
    if file_extension not in allowed_extensions:
        return json.dumps({'error': f"File should have one of {allowed_extensions} extensions"}), 400

    filename = str(uuid.uuid4()) + file_extension

    
    filepath = os.path.join('imageStorage', filename)
    file.save(filepath)

    return json.dumps({'result': model.get_prediction(filepath) })



if __name__ == '__main__':
    app.run(debug=True)
