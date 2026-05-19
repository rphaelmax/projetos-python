from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('questao1.html', nome = "Raphael")

@app.route('/alunos')
def alunos():
    alunos = [
        {"nome": "Fred", "idade": 18}, 
        {"nome": "Antonio", "idade": 20}, 
        {"nome": "Jamal", "idade": 25}
        ]
    return render_template('questao2.html', alunos = alunos)

@app.route('/usuario')
def usuario():
    usuario = {"nome": "Ana", "email": "ana@email.com"}
    return render_template('questao3.html', usuario = usuario)

@app.route('/lista')
def lista_nomes():
    nomes = ["Raphael", "Rian", "Fred", "Paulo"]
    return render_template('questao4.html', nomes = nomes)

@app.route('/notas')
def notas():
    lista_alunos = [
        {"nome": "Raphael", "nota": 10},
        {"nome": "Pedro", "nota": 5},
        {"nome": "Antonio", "nota": 7}
    ]
    return render_template('questao5.html', alunos = lista_alunos)

if __name__ == '__main__':
    app.run(debug=True)