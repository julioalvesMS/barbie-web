from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename

import tempfile
import os.path
import sys
import traceback

from back import barbiefy

app = Flask(__name__)

@app.route('/')
def DefaultCodeSubmissionPage():
    return app.send_static_file('home.html')

@app.route('/submit', methods=['POST'])
def BarbieSubmissionPage():
    # Make a unique temporary folder for this submission
    temp_dir = tempfile.mkdtemp(prefix='barbie')
    # Use a dict to save all of run_and_comparethe files, separated by extension
    _files = dict()
    for key in request.files:
        f = request.files[key]
        path = os.path.join(temp_dir, secure_filename(f.filename))
        # Save the file
        f.save(path)
        # Get extension
        ext = os.path.splitext(path)[1][1:].strip()
        if ext not in _files:
            _files[ext] = list()
        # Save in the dict the path to this file
        _files[ext].append(path)
    with open('out.txt', 'w+') as txt:
        sys.stdout = txt
        try:
            barbiefy(temp_dir, _files['c'], request.form['disciplina'], request.form['turma'], request.form['lab'])
        except:
            aux = sys.exc_info()[2]
            print('Erro')
            traceback.print_exception(aux[0], aux[1], aux[2])
        aux = txt.read()
    return aux
