from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)
app.secret_key = 'kimera'
class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo('Super Mario Bros', 'Ação', 'Nitendo')
jogo2 = Jogo('The Wicher', 'Aventura', 'Pc')
jogo3 = Jogo('Super Mario', 'Ação', 'Wii')

games = [jogo1, jogo2, jogo3]

senha_padrao = 'admin'


@app.route('/')
def index():
    return render_template('lista.html', titulo='Games', jogos=games)


@app.route('/novo')
def novo():

    if session['usuario_logado'] is None or 'usuario_logado' not in session:
        return redirect(url_for('login', proxima=url_for('novo')))
    else:
        return render_template('novo.html', titulo ='Novo Game')


@app.route('/criar', methods=['POST', ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogo(nome, categoria, console)
    games.append(jogo)
    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if senha_padrao == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + ' logou com sucesso!')
        proxima_pagina = request.form['proxima']
        return redirect(proxima_pagina)
    else:
        flash('Usuario ou senha invalidos, tente novamente!')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout feito com sucesso!')
    return redirect(url_for('login'))


app.run(debug=True)