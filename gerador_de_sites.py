# Importa as bibliotecas necessárias
import os
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QCheckBox, QPushButton, QMessageBox

# Inicializa a aplicação
app = QApplication([])

# Define a classe da janela do gerador de projeto
class GeradorProjeto(QWidget):
    def __init__(self):
        super().__init__()

        # Configurações iniciais da janela
        self.setWindowTitle("Gerador de Projeto Web")
        self.setGeometry(100, 100, 400, 350)

        # Inicializa a interface do usuário
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Criação da interface do usuário:
        
        # Campo para digitar o nome do projeto
        self.label_nome_projeto = QLabel("Digite o nome do projeto:")
        self.nome_projeto = QLineEdit()
        layout.addWidget(self.label_nome_projeto)
        layout.addWidget(self.nome_projeto)

        # Caixas de seleção para escolher os tipos de arquivos a serem criados
        self.label_arquivos = QLabel("Selecione os tipos de arquivos:")
        self.checkbox_html = QCheckBox("HTML")
        self.checkbox_css = QCheckBox("CSS")
        self.checkbox_js = QCheckBox("JavaScript")
        layout.addWidget(self.label_arquivos)
        layout.addWidget(self.checkbox_html)
        layout.addWidget(self.checkbox_css)
        layout.addWidget(self.checkbox_js)

        # Caixas de seleção para escolher o conteúdo do HTML
        self.label_conteudo_html = QLabel("Selecione o conteúdo do HTML:")
        self.checkbox_head = QCheckBox("Head")
        self.checkbox_body = QCheckBox("Body")
        self.checkbox_footer = QCheckBox("Footer")
        layout.addWidget(self.label_conteudo_html)
        layout.addWidget(self.checkbox_head)
        layout.addWidget(self.checkbox_body)
        layout.addWidget(self.checkbox_footer)

        # Botão GERAR para iniciar a criação do projeto
        self.button_gerar = QPushButton("GERAR")
        layout.addWidget(self.button_gerar)

        # Conecta o botão "GERAR" a uma função que gera o projeto
        self.button_gerar.clicked.connect(self.gerar_projeto)

        # Define o layout da janela
        self.setLayout(layout)

    # Função para gerar o projeto com base nas seleções do usuário
    def gerar_projeto(self):
        # Obtém o nome do projeto inserido pelo usuário
        nome_projeto = self.nome_projeto.text()
        # Verifica se as caixas de seleção para criar arquivos HTML, CSS e JavaScript estão marcadas
        criar_html = self.checkbox_html.isChecked()
        criar_css = self.checkbox_css.isChecked()
        criar_js = self.checkbox_js.isChecked()
        # Verifica quais partes do conteúdo HTML devem ser incluídas
        incluir_head = self.checkbox_head.isChecked()
        incluir_body = self.checkbox_body.isChecked()
        incluir_footer = self.checkbox_footer.isChecked()

        # Verifica se um nome para o projeto foi inserido
        if not nome_projeto:
            QMessageBox.critical(self, "Erro", "Por favor, insira um nome para o projeto.")
            return

        # Cria o diretório do projeto
        if not os.path.exists(nome_projeto):
            os.makedirs(nome_projeto)

        # Gera os arquivos HTML, CSS e JavaScript com base nas seleções do usuário
        if criar_html:
            with open(os.path.join(nome_projeto, "index.html"), "w") as html_file:
                html_content = "<!DOCTYPE html>\n<html>"
                if incluir_head:
                    html_content += "\n<head>"
                    html_content += "\n    <title>{}</title>".format(nome_projeto)
                    # Adiciona as tags <link> para CSS e <script> para JavaScript, se selecionados
                    if criar_css:
                        html_content += "\n    <link rel='stylesheet' href='style.css'>"
                    if criar_js:
                        html_content += "\n    <script src='script.js'></script>"
                    html_content += "\n</head>"
                if incluir_body:
                    html_content += "\n<body>"
                    html_content += "\n    <h1>Conteúdo do Body</h1>"
                    html_content += "\n</body>"
                if incluir_footer:
                    html_content += "\n<footer>"
                    html_content += "\n    <p>Rodapé</p>"
                    html_content += "\n</footer>"
                html_content += "\n</html>"
                html_file.write(html_content)

        if criar_css:
            with open(os.path.join(nome_projeto, "style.css"), "w") as css_file:
                css_file.write("/* Estilos CSS para {} */".format(nome_projeto))

        if criar_js:
            with open(os.path.join(nome_projeto, "script.js"), "w") as js_file:
                js_file.write("// JavaScript para {} - Adicione seu código aqui".format(nome_projeto))

        # Exibe uma mensagem de sucesso após a geração do projeto
        QMessageBox.information(self, "Sucesso", "Projeto gerado com sucesso em '{}'".format(nome_projeto))

# Inicializa a janela principal do aplicativo
if __name__ == "__main__":
    window = GeradorProjeto()
    window.show()
    app.exec()
