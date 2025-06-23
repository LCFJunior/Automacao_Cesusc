# 🧾 Gerador de PDF - Notas e Frequências CESUSC (Modo CSV)

Este é um aplicativo desktop em Python com interface gráfica (Tkinter) que automatiza o processo de login no portal acadêmico do CESUSC, acessa a seção de **Notas e Frequências** e gera automaticamente um **PDF com o boletim de múltiplos alunos** a partir de um arquivo **CSV**.

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## ✨ Funcionalidades

✅ Leitura de múltiplas matrículas e senhas via CSV  
✅ Login automatizado no portal do CESUSC  
✅ Acesso direto às Notas e Frequências  
✅ Geração de PDF automaticamente via navegador  
✅ Seleção de pasta para salvar os arquivos  
✅ Mensagens de erro e sucesso para cada aluno  
✅ Animação de carregamento com GIF  
✅ Interface gráfica simples e funcional  

---

## 🖼️ Interface

> A interface foi feita com Tkinter e inclui um botão para selecionar o arquivo `.csv` e iniciar o processo de geração dos boletins em lote, além de exibir o status atual e animação de carregamento.

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
   ```bash
   git clone https://github.com/LCFJunior/Automacao_Cesusc.git
   cd Automacao_Cesusc
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Prepare o arquivo `alunos.csv` contendo as **credenciais dos alunos**, uma por linha, no seguinte formato:
   ```
   matricula1, senha1
   matricula2, senha2
   ```

   > Exemplo:
   ```
   1234567, senha123
   7654321, 321senha
   ```

4. Execute o script:
   ```bash
   python cesusc.py
   ```

5. Na interface que abrir:
   - Clique em **"Selecionar CSV de Alunos"**
   - Selecione o arquivo `.csv`
   - Escolha a pasta onde deseja salvar os PDFs
   - Aguarde o processo automático para cada aluno

---

## 📁 Estrutura esperada

```bash
Automacao_Cesusc/
├── alunos.csv                # Arquivo com credenciais (um por linha)
├── loading.gif              # Animação de carregamento (obrigatória)
├── main.py                  # Código principal
├── README.md                # Este arquivo
└── requirements.txt         # Lista de dependências
```

---

## 📌 Requisitos

- Python 3.10 ou superior  
- Navegador **Google Chrome** instalado no sistema

---

## 📜 Licença

Este projeto está sob a licença [MIT](https://opensource.org/licenses/MIT).
