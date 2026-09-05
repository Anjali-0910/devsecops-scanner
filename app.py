import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def get_existing_files():
    """Helper function to scan the uploads folder and list all files"""
    file_list = []
    for root, dirs, files in os.walk(app.config['UPLOAD_FOLDER']):
        for file in files:
            full_path = os.path.join(root, file)
            # Get relative path so it looks clean in the table
            rel_path = os.path.relpath(full_path, app.config['UPLOAD_FOLDER'])
            file_list.append({
                'name': file,
                'path': rel_path
            })
    return file_list

@app.route('/')
def home():
    # Automatically load any files already sitting in the uploads folder
    existing_files = get_existing_files()
    return render_template('index.html', uploaded_files=existing_files, total_files=len(existing_files))

@app.route('/upload', methods=['POST'])
def upload_file():
    files = request.files.getlist('folder')
    if not files or files[0].filename == '':
        return redirect(request.url)
    
    saved_count = 0
    for file in files:
        if file.filename:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            file.save(filepath)
            saved_count += 1
    
    # Fetch all files currently in the folder after upload
    all_files = get_existing_files()
    status_msg = f"Successfully ingested {saved_count} files. Total stored: {len(all_files)} files."
    
    return render_template('index.html', message=status_msg, total_files=len(all_files), uploaded_files=all_files)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)