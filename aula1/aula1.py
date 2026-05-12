from flask import Flask

app = Flask(__name__) # inicio o flask

@app.route('/decorator') # Isso é outro decorator, mapeando a função abaixo para a rota desejada
def deco():
    return """
    <!doctype html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Decorator em Python</title>
   </head>
    <body>
        <h1>O que é um decorator em Python</h1>
        <p>Um decorator é uma função que recebe outra função (ou classe) e retorna uma nova função com comportamento estendido, sem alterar o código original da função decorada.</p>
        <h2>Para que ele serve</h2>
        <p>Serve para reutilizar lógica transversal (como logging, autenticação, caching), compor funcionalidades e aplicar alterações de comportamento de forma limpa e reutilizável.</p>
        <h2>Como é utilizado no Flask</h2>
        <p>No Flask, decorators são usados para mapear rotas (por exemplo @app.route('/')) e para aplicar wrappers a views (por exemplo @login_required), permitindo executar lógica antes ou depois da função de view.</p>
    </body>
    </html>"""

if __name__ == '__main__':
    app.run(debug=True) # Isso inicia o servidor Flask em modo de depuração, o que é útil para desenvolvimento
