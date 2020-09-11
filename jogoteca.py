from flask import Flask, render_template, request, redirect

app = Flask(__name__)
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
    return render_template('novo.html', titulo ='Novo Game')


@app.route('/criar', methods=['POST', ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogo(nome, categoria, console)
    games.append(jogo)
    return redirect('/')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if senha_padrao == request.form['senha']:
        return redirect('/')
    else:
        return redirect('/login')


app.run(debug=True)