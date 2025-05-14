from flask import Flask, render_template, request, send_from_directory, redirect, url_for
import os
from utils import encrypt_image_flow, decrypt_image_flow, predict_image_label, get_domain_from_label

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    image = request.files['image']
    password = request.form['password']
    image_path = os.path.join(UPLOAD_FOLDER, image.filename)
    image.save(image_path)

    output_path = encrypt_image_flow(image_path, password)
    label = predict_image_label(image_path)
    domain = get_domain_from_label(label)

    return render_template("result.html", 
                           image_file=os.path.basename(output_path), 
                           label=label, 
                           domain=domain)

@app.route('/decrypt', methods=['POST'])
def decrypt():
    image = request.files['image']
    password = request.form['password']
    image_path = os.path.join(UPLOAD_FOLDER, image.filename)
    image.save(image_path)

    output_path = decrypt_image_flow(image_path, password)

    return render_template("result.html", 
                           image_file=os.path.basename(output_path), 
                           label="N/A", 
                           domain="N/A")

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
