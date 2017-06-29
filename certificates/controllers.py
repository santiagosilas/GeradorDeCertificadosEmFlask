from os.path import join
from werkzeug import secure_filename
from certificates import app, utils
from flask import request, render_template

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        file = request.files['file']
        curso = request.form['curso']
        nomes = request.form['nomes'].split('\n')
        if file:
            filename = secure_filename(file.filename)
            saved_path = join(join(app.config['UPLOADS'],'default'), filename)
            file.save(saved_path)
            utils.create_certificate(saved_path,curso,nomes)
            return 'certificados gerados com sucesso!'
        else:
        	return 'erro no upload do arquivo'
    return render_template('index.html')