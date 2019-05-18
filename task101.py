
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

FOLDER1 = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['xls', 'xlsx', 'csv'])

app = Flask(__name__)
app.config['FOLDER1'] = FOLDER1

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
       
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
       
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['FOLDER1'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>NEW FILE</title>
    <h1>UPLOAD IT HERE</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''