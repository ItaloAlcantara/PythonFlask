from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio')
def ola():
    lista = ['Tetris','League of legends', 'The witcher']
    return render_template('lista.html',titulo='Games', jogos = lista)

app.run()