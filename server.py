from flask import Flask, render_template, request, url_for, make_response, abort
from werkzeug.utils import secure_filename

import tempfile
import os.path
import sys
import traceback

from back import barbiefy, timedCleanUp

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route('/')
def DefaultCodeSubmissionPage():
    return app.send_static_file('home.html')

@app.route('/submit', methods=['POST'])
def BarbieSubmissionPage():
    # Make a unique temporary folder for this submission
    temp_dir = tempfile.mkdtemp(prefix='barbie')
    timedCleanUp(temp_dir)
    submission_id = os.path.basename(temp_dir)
    # Use a dict to save all of run_and_comparethe files, separated by extension
    _files = dict()

    fd, txt_path = tempfile.mkstemp(dir=temp_dir, text=True)
    os.close(fd)
    txt = open(txt_path, 'w')
    stderr, sys.stderr = sys.stderr, txt

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

    try:
        assert 'c' in _files, 'Nenhum arquivo .c fornecido'
        results = barbiefy(temp_dir, _files['c'], request.form['disciplina'], request.form['turma'], request.form['lab'])
        assert results, 'Falha durante o processamento'
    except:
        aux = sys.exc_info()[1]
        print('Erro: Execução interrompida:\n' + str(aux), file=sys.stderr)
        results = list()

    sys.stderr = stderr
    txt.close()

    txt = open(txt_path, 'r')
    output = txt.read()
    txt.close()

    if not output:
        output = 'Nenhum problema encontrado durante a execução'

    return render_template('result.html', output=output, results=results, submission_id=submission_id)

@app.route('/output/<submission_id>/<index>/<file_type>')
def RetrieveFile(submission_id, index, file_type):
    try:
        f = open(os.path.join('/tmp', submission_id, 'testes', index, 'arq%s.%s' % (index, file_type)), 'r')
        msg = f.read()
        f.close()
        resp = make_response(msg)
        resp.headers['content-type'] = 'text/plain'
    except IOError:
        abort(404)
    return resp

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
