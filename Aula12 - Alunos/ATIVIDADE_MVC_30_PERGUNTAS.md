# Atividade Aula 12 — Model, Controller e View (StreamFlix)

**Disciplina:** Python / Flask  
**Profª:** Janaína Duarte  
**Projeto:** `flask/Aula12/`  
**Objetivo:** Explorar o código, localizar arquivos e explicar o que cada camada faz.

---

## Como responder

1. Abra a pasta `flask/Aula12/` no editor ou GitHub.
2. Navegue pelas pastas `models/`, `controllers/` e `views/`.
3. Rode o site (`python app.py`) quando a pergunta pedir para testar no navegador.
4. Responda com **caminho do arquivo** + **explicação em suas palavras**.

**Identificação**

- Nome: Raphael Max Alves Jacomo
- Turma: 3C2

---

## Bloco A — Model (perguntas 1 a 10)

**1.** Em qual pasta ficam as classes que representam tabelas do banco SQLite? Cite o caminho.
Pasta dos modelos
Caminho: Aula12 - Alunos/models/
Explicação: é nessa pasta que ficam as classes que representam as tabelas do banco SQLite, como FilmeFavorito e HistoricoBusca.

**2.** Qual é o nome do arquivo de banco criado quando o app roda? Em qual arquivo Python essa configuração está?
Nome do arquivo de banco: streamflix.db
Arquivo Python que configura: Aula12 - Alunos/app.py
Explicação: em app.py, a linha app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(pasta, "streamflix.db") define o caminho do banco.

**3.** Quais classes Model existem no projeto (nome das classes)? Em quais arquivos `.py` cada uma está?
Classes Model e arquivos
FilmeFavorito em Aula12 - Alunos/models/filme_favorito.py
HistoricoBusca em Aula12 - Alunos/models/historico_busca.py
Explicação: são as duas classes que representam tabelas locais do app.

**4.** De qual superclasse `FilmeFavorito` e `HistoricoBusca` herdam? O que elas ganham automaticamente por herança (cite 3 campos)?
Herança: ambas herdam de ModeloBase
Arquivo da superclasse: Aula12 - Alunos/models/base.py
Campos ganhos automaticamente:
id
data_criacao
data_atualizacao
Explicação: ModeloBase é abstrata (__abstract__ = True) e fornece esses campos comuns a todas as tabelas locais.

**5.** Qual é o `__tablename__` da tabela de favoritos? Por que usamos `__tablename__` em vez de só o nome da classe?
__tablename__ da tabela de favoritos
Valor: filmes_favoritos
Por que usar __tablename__: para definir explicitamente o nome da tabela no banco. Sem isso, o SQLAlchemy tenta inferir o nome da tabela a partir da classe, mas aqui o objetivo é ter um nome claro e específico (filmes_favoritos), além de evitar ambiguidade.

**6.** No model `FilmeFavorito`, qual coluna guarda o id do filme vindo da API TMDB? Ela tem alguma restrição especial (`unique`, `nullable`)?
Coluna: tmdb_id
Restrições: nullable=False e unique=True
Explicação: essa coluna guarda o id do filme vindo da API TMDB e garante que cada filme favorito só exista uma vez.

**7.** Abra `models/filme_favorito.py`. O que o método `@classmethod adicionar` faz passo a passo? O que acontece se o filme já existir nos favoritos?
O que FilmeFavorito.adicionar faz
Arquivo: Aula12 - Alunos/models/filme_favorito.py
Passo a passo:
chama buscar_por_tmdb(tmdb_id) para ver se o filme já existe nos favoritos;
se já existir, retorna None e não cria um novo registro;
se não existir, cria uma instância fav = cls(...) com tmdb_id, titulo, poster_path, nota e ano;
adiciona a instância à sessão com db.session.add(fav);
grava no banco com db.session.commit();
retorna o objeto favorito criado.
O que acontece se já existir: ele não adiciona novamente; retorna None.

**8.** Onde está o método que lista as últimas 8 buscas? Qual é o nome da classe e do método?
Classe: HistoricoBusca
Método: ultimas
Arquivo: Aula12 - Alunos/models/historico_busca.py
Explicação: esse método faz cls.query.order_by(cls.data_criacao.desc()).limit(limite).all() para buscar os últimos registros ordenados por data.

**9.** O model grava dados da API TMDB inteira ou só alguns campos espelhados? Cite 4 campos salvos em `FilmeFavorito`.
O model grava só alguns campos espelhados, não a API inteira.
Quatro campos salvos em FilmeFavorito:
tmdb_id
titulo
poster_path
nota
ano
Explicação: o modelo representa apenas os dados relevantes para exibir e identificar o favorito, e não o JSON completo da API.

**10.** Em `models/__init__.py`, o que é exportado além de `db`? Por que o controller importa `from models import FilmeFavorito` em vez de importar o arquivo inteiro da pasta?
Exportado além de db:
ModeloBase
FilmeFavorito
HistoricoBusca
Explicação do import no controller: o controller usa from models import FilmeFavorito porque models/__init__.py já expõe essa classe no pacote, tornando o import mais simples e limpo do que importar diretamente o arquivo models/filme_favorito.py.

---

## Bloco B — Controller (perguntas 11 a 20)

**11.** Quantos Blueprints existem no projeto? Cite o **nome** de cada um e o **url_prefix** (se tiver).

- Existem 3 Blueprints.
- `dashboard_bp` em `controllers/dashboard_controller.py`, sem `url_prefix`.
- `filmes_bp` em `controllers/filmes_controller.py`, com `url_prefix="/filmes"`.
- `favoritos_bp` em `controllers/favoritos_controller.py`, com `url_prefix="/favoritos"`.

**12.** Em qual arquivo está a rota `/filmes/populares`? Qual é o nome da função Python que responde essa URL?

- Arquivo: `controllers/filmes_controller.py`.
- Função: `populares()`.

**13.** O que a função `populares()` faz antes de chamar `render_template`? Cite duas chamadas (Model, Service ou API).

- Chama `TmdbApi().filmes_populares()` para buscar a lista de filmes populares (Service/API).
- Chama `FilmeFavorito.listar()` (Model) para obter os favoritos atuais e montar `ids_fav`.

**14.** Quando o usuário busca um filme em `/filmes/buscar`, qual controller registra o termo no banco? Qual model é usado e em qual linha aproximada?

- Controller: `filmes_controller.py`, função `buscar()`.
- Model: `HistoricoBusca` em `models/historico_busca.py`.
- Linha aproximada: dentro de `buscar()`, no `if termo:` que chama `HistoricoBusca.registrar(termo, len(filmes))`.

**15.** Abra `controllers/favoritos_controller.py`. Qual método HTTP é exigido para adicionar favorito (`GET` ou `POST`)? Qual a URL completa de exemplo para adicionar o filme id 550?

- Método HTTP: `POST`.
- URL de exemplo: `/favoritos/adicionar/550`.

**16.** No `filmes_controller.py`, rota `detalhe(filme_id)`: o que acontece se `api.detalhe(filme_id)` retornar `None`?

- O controller redireciona o usuário para `url_for("filmes.populares")`, ou seja, volta para a lista de filmes populares.

**17.** Onde os Blueprints são **registrados** no Flask? Cite o arquivo e o comando usado (3 registros).

- Arquivo: `app.py`.
- Comandos:
  - `app.register_blueprint(dashboard_bp)`
  - `app.register_blueprint(filmes_bp)`
  - `app.register_blueprint(favoritos_bp)`

**18.** Qual controller cuida da página inicial `/`? Quais variáveis ele envia para o template `index.html`?

- Controller: `dashboard_controller.py`, função `index()`.
- Variáveis enviadas: `populares`, `melhores`, `total_favoritos`, `historico`, `modo_demo`.

**19.** A pasta `services/tmdb_api.py` é Model, Controller ou View? Justifique: quem chama essa classe e para quê?

- É um Service (serviço de API).
- Justificativa: não define rotas nem templates; fornece acesso a dados externos da API TMDB e formata filmes.
- Quem chama: controllers (`dashboard_controller.py` e `filmes_controller.py`) usam `TmdbApi` para buscar filmes, detalhes e streaming.

**20.** No controller de busca, de onde vem o termo digitado quando o usuário usa o formulário da home (`index.html`)? É `request.form` ou `request.args`? Explique a diferença nesse projeto.

- O termo vem de `request.args.get("q", "")` quando a requisição é GET.
- Se o formulário for enviado por POST, o controller usa `request.form.get("q", "")`.
- Explicação: o código primeiro pega o termo em `request.args` para buscas via query string e só usa `request.form` quando o método é POST, permitindo suportar ambos os tipos de envio.

---

## Bloco C — View (perguntas 21 a 30)

**21.** Onde ficam os templates HTML? Qual caminho completo da pasta?

- Caminho completo: `Aula12 - Alunos/views/templates/`
- Explicação: todos os arquivos HTML usados pelo Flask estão dentro dessa pasta e suas subpastas `favoritos/` e `filmes/`.

**22.** Qual template é a “base” de todas as páginas (layout com menu)? Como os outros templates usam esse layout (qual comando Jinja)?

- Template base: `views/templates/layout.html`.
- Os outros templates usam esse layout com `{% extends "layout.html" %}` e preenchem a seção com `{% block content %}`.

**23.** Abra `views/templates/layout.html`. Liste os 5 links do menu e o `url_for` de cada um.

- `StreamFlix` → `url_for('dashboard.index')`
- `Populares` → `url_for('filmes.populares')`
- `Melhores` → `url_for('filmes.melhores')`
- `Buscar` → `url_for('filmes.buscar')`
- `Favoritos` → `url_for('favoritos.listar')`

**24.** Qual arquivo HTML exibe a seção **“Onde assistir (Brasil)”**? De onde vem a variável `streaming` usada nessa tela?

- Arquivo: `views/templates/filmes/detalhe.html`.
- A variável `streaming` vem do controller `filmes_controller.py`, função `detalhe()`, que chama `TmdbApi().streaming(filme_id)`.

**25.** O arquivo `filmes/_card.html` é uma página inteira ou um pedaço reutilizado? Quem inclui esse arquivo e com qual tag Jinja?

- `filmes/_card.html` é um pedaço reutilizado (partial), não uma página inteira.
- Ele é incluído por `views/templates/filmes/lista.html` usando `{% include "filmes/_card.html" %}`.

**26.** Em `filmes/detalhe.html`, como a View sabe se o filme já está nos favoritos? Qual variável booleana/objeto controla o botão “Salvar” vs “Remover”?

- A view usa a variável `favorito` passada pelo controller.
- Em `detalhe.html`, há `{% if favorito %}`; se existir objeto `favorito`, mostra o botão “★ Remover dos favoritos”, caso contrário mostra o botão “★ Salvar favorito”.

**27.** Onde está o CSS do site? Como o `layout.html` carrega esse arquivo (função Flask/Jinja)?

- O CSS está em `Aula12 - Alunos/views/static/css/style.css`.
- O `layout.html` carrega com `<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">`.

**28.** Na listagem de favoritos (`favoritos/lista.html`), qual loop Jinja percorre os registros? Cite 3 campos exibidos na tabela.

- Loop: `{% for fav in favoritos %}`
- Campos exibidos: `fav.titulo`, `fav.nota`, `fav.ano`, `fav.data_criacao.strftime('%d/%m/%Y')`.

**29.** O que significa `{% if modo_demo %}` no layout? Quem disponibiliza essa variável para **todos** os templates?

- Significa que o site está em modo demonstração quando não há chave TMDB configurada.
- A variável é disponibilizada por `app.py` no `@app.context_processor` chamado `inject_globals()`, que retorna `{'modo_demo': TmdbApi().usando_demo}`.

**30.** Desenhe ou descreva o fluxo completo quando o aluno clica em **“Salvar favorito”** no detalhe do filme, indicando **View → Controller → Model** (e redirect de volta). Cite arquivos envolvidos.

- View: `views/templates/filmes/detalhe.html` exibe o botão e o formulário POST para `url_for('favoritos.adicionar', tmdb_id=filme.id)`.
- Controller: a rota `favoritos.adicionar` em `controllers/favoritos_controller.py` recebe o POST, lê `titulo`, `poster_path`, `nota`, `ano` e `voltar` do formulário, e chama `FilmeFavorito.adicionar(...)`.
- Model: `models/filme_favorito.py` realiza `FilmeFavorito.adicionar(...)`, verifica se o filme já existe com `buscar_por_tmdb`, adiciona o novo favorito à sessão com `db.session.add(fav)` e salva com `db.session.commit()`.
- Redirect: após salvar, o controller redireciona de volta para a página do detalhe usando o valor de `voltar` ou `url_for('favoritos.listar')`.

---

## Entrega

- Arquivo `.txt` ou `.md` com as 30 respostas 

**Critério:** respostas que mostrem que você **abriu o código**, não chute.

Boa exploração!
