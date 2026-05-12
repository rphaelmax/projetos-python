from flask import Flask

app = Flask(__name__)

@app.route('/curriculo')
def home():
    return '''
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Currículo</title>
            <style>
                :root{
                    --bg:#f4f7fb;
                    --card:#ffffff;
                    --muted:#6b7280;
                    --accent:#2563eb;
                    --shadow: 0 4px 12px rgba(16,24,40,0.06);
                }
                *{box-sizing:border-box}
                body{
                    margin:0;
                    font-family: Inter, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
                    background:var(--bg);
                    color:#0f172a;
                    -webkit-font-smoothing:antialiased;
                    -moz-osx-font-smoothing:grayscale;
                }
                .wrap{
                    max-width:900px;
                    margin:40px auto;
                    padding:24px;
                }
                header{
                    display:flex;
                    align-items:center;
                    gap:16px;
                    margin-bottom:20px;
                }
                header h1{
                    margin:0;
                    font-size:28px;
                    color:var(--accent);
                }
                .card{
                    background:var(--card);
                    padding:18px;
                    border-radius:10px;
                    box-shadow:var(--shadow);
                    margin-bottom:16px;
                    border:1px solid rgba(15,23,42,0.04);
                }
                h2{
                    margin:0 0 10px 0;
                    font-size:18px;
                }
                ul{
                    margin:0;
                    padding:0;
                    list-style:none;
                }
                li{
                    margin-bottom:8px;
                    color:var(--muted);
                }
                li strong{
                    color:#0f172a;
                    width:120px;
                    display:inline-block;
                }
                .meta{
                    display:flex;
                    flex-wrap:wrap;
                    gap:12px 24px;
                }
                @media (max-width:600px){
                    .wrap{padding:16px; margin:20px;}
                    header h1{font-size:22px;}
                    li strong{display:block; width:auto;}
                }
            </style>
        </head>
        <body>
            <div class="wrap">
                <header>
                    <h1>Currículo</h1>
                </header>

                <section class="card">
                    <h2>Informações Pessoais</h2>
                    <ul class="meta">
                        <li><strong>Nome:</strong> Raphael Max</li>  
                        <li><strong>Email:</strong> raphaelmax@gmail.com</li>
                        <li><strong>Telefone:</strong> (31) 99999-9999</li>
                    </ul>
                </section>

                <section class="card">
                    <h2>Experiência Profissional</h2>
                    <ul>
                        <li><strong>Empresa:</strong> Garena Free Fire</li>
                        <li><strong>Cargo:</strong> Desenvolvedor de Software</li>
                        <li><strong>Período:</strong> Jan 2024 - Presente</li>
                    </ul>
                </section>
            </div>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)