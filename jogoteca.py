from flask import Flask, render_template

app = Flask(__name__)
class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


@app.route('/inicio')
def ola():
    jogo1 = Jogo('Super Mario Bros', 'Ação', 'Nitendo')
    jogo2 = Jogo('The Wicher', 'Aventura', 'Pc')
    jogo3 = Jogo('Super Mario', 'Ação', 'Wii')

    games = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo='Games', jogos=games)

app.run()