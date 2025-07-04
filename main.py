from flask import Flask, render_template, request, send_file
import os
from werkzeug.utils import secure_filename
from utils import generate_key
from encryptor import encrypt_file
from decryptor import decrypt_file

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        uploaded_file = request.files['file']
        password = request.form['password']
        action = request.form['action']

        if uploaded_file and password:
            filename = secure_filename(uploaded_file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            uploaded_file.save(filepath)

            try:
                key = generate_key(password)
                if action == 'encrypt':
                    result_path = encrypt_file(filepath, key)
                    message = "File encrypted successfully!"
                elif action == 'decrypt':
                    result_path = decrypt_file(filepath, key)
                    message = "File decrypted successfully!"
                else:
                    message = "Invalid action."
                    result_path = None

                return send_file(result_path, as_attachment=True)
            except Exception as e:
                message = f"Error: {e}"
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
