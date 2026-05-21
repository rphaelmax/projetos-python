from flask import Flask, request, render_template_string

app = Flask(__name__)

def show_the_login_form():
    return render_template_string("""
        <h2>Login</h2>
        <form method="POST">
            <input type="text" name="usuario" placeholder="Usuário"><br><br>
            <input type="password" name="senha" placeholder="Senha"><br><br>
            <button type="submit">Entrar</button>
        </form>
    """)

def do_the_login():
    usuario_input = request.form.get('usuario')
    senha_input = request.form.get('senha')

    usuarios = [
        {"nome": "raphael", "senha": "22400664"},
        {"nome": "dolga", "senha": "cotemig2026"},
        {"nome": "janaina", "senha": "cotemig2026"},
        {"nome": "antonio", "senha": "cotemig2026"}
    ]

    for u in usuarios:
        if u["nome"] == usuario_input and u["senha"] == senha_input:
            return f"<h1>Bem-vindo, {u['nome']}!</h1>"
        
    return "Acesso negado!"
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

if __name__ == "__main__":
    app.run(debug=True)

# site de consulta https://flask.palletsprojects.com/en/stable/quickstart/#html-escaping