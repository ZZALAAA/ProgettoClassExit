from flask import Flask, render_template, request, redirect, url_for
from tinydb import TinyDB, Query

app = Flask(__name__)
db = TinyDB('database.json')
Alunno = Query()

@app.route('/')
def index():
    registro = db.all()
    return render_template('index.html', registro=registro)

@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    nome = request.form['nome']
    cognome = request.form['cognome']
    data = request.form['data']
    ora = request.form['ora']
    giustificazione = request.form['giustificazione']
    db.insert({'nome': nome, 'cognome': cognome, 'data': data, 'ora': ora, 'giustificazione': giustificazione})
    return redirect(url_for('index'))

@app.route('/modifica/<int:id>', methods=['POST'])
def modifica(id):
    nome = request.form['nome']
    cognome = request.form['cognome']
    data = request.form['data']
    ora = request.form['ora']
    giustificazione = request.form['giustificazione']
    db.update({'nome': nome, 'cognome': cognome, 'data': data, 'ora': ora, 'giustificazione': giustificazione}, doc_ids=[id])
    return redirect(url_for('index'))

@app.route('/elimina/<int:id>', methods=['POST'])
def elimina(id):
    db.remove(doc_ids=[id])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)