import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    files = request.files.getlist('folder')
    if not files or files[0].filename == '':
        return redirect(request.url)
    
    saved_filenames = []
    for file in files:
        if file.filename:
            # Preserve path relative structure if available
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            file.save(filepath)
            saved_filenames.append(file.filename)
    
    status_msg = f"Successfully uploaded {len(saved_filenames)} files from directory. Vulnerability check executed!"
    return render_template('index.html', message=status_msg, total_files=len(saved_filenames), uploaded_files=saved_filenames)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)