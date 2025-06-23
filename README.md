# 🧾 Gerador de PDF - Notas e Frequências CESUSC

Este é um aplicativo desktop em Python com interface gráfica (Tkinter) que automatiza o processo de login no portal acadêmico do CESUSC, acessa a seção de **Notas e Frequências** e gera automaticamente um **PDF com seu boletim**.

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## ✨ Funcionalidades

✅ Interface amigável e simples para alunos  
✅ Login automatizado no portal do CESUSC  
✅ Acesso direto às Notas e Frequências  
✅ Geração de PDF automaticamente via navegador  
✅ Seleção de pasta para salvar o arquivo  
✅ Mensagens de erro e sucesso  
✅ Animação de carregamento com GIF

---

## 🖼️ Interface

> A interface foi feita com Tkinter e inclui campos de matrícula, senha, botão para exibir/ocultar senha, botão de execução e uma animação com GIF durante o carregamento do processo.

---

## 🧪 Tecnologias Utilizadas

- [Python 3](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [Selenium](https://www.selenium.dev/)
- [Pillow (PIL)](https://pillow.readthedocs.io/)
- [webdriver-manager](https://pypi.org/project/webdriver-manager/)

---

## ⚙️ Como usar

1. Clone este repositório:
   
bash
   git clone https://github.com/seu-usuario/gerador-pdf-cesusc.git
   cd gerador-pdf-cesusc

2. Instale as dependências:
bash
   pip install -r requirements.txt

3. Execute o script:
   
bash
   python cesusc.py

4. Preencha sua matrícula e senha, escolha a pasta onde deseja salvar o PDF e aguarde a geração automática.

## 📁 Estrutura esperada
bash
  gerador-pdf-cesusc/
  ├── loading.gif               # Animação de carregamento (obrigatória)
  ├── main.py                   # Código principal
  ├── README.md                 # Este arquivo
  └── requirements.txt          # Lista de dependências
## 📌 Requisitos
- Python 3.10 ou superior
- Navegador Google Chrome instalado no sistema
