import os
import threading
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import datetime
import time
import shutil
import glob

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Função para carregar todos os frames do GIF animado
def carregar_gif_animado(caminho_gif):
    frames = []
    gif = Image.open(caminho_gif)
    try:
        while True:
            frames.append(ImageTk.PhotoImage(gif.copy()))
            gif.seek(gif.tell() + 1)
    except EOFError:
        pass
    return frames

# Função para animar o GIF no label
def animar_gif(label, frames, index=0):
    frame = frames[index]
    label.config(image=frame)
    index = (index + 1) % len(frames)
    label.after(100, animar_gif, label, frames, index)

def rodar_script(usuario, senha, pasta_destino):
    try:
        # Ativa o status e gif antes de rodar
        def ativar_loading():
            status_var.set("Processando...")
            gif_label.pack(pady=10)
        janela.after(0, ativar_loading)

        # Cria pasta temporária para o PDF
        temp_dir = os.path.join(os.getcwd(), "temp_pdf")
        os.makedirs(temp_dir, exist_ok=True)

        # Configurações do Chrome
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("prefs", {
            "printing.print_preview_sticky_settings.appState": r"""
            {
                "recentDestinations": [{"id": "Save as PDF", "origin": "local", "account": ""}],
                "selectedDestinationId": "Save as PDF",
                "version": 2
            }
            """,
            "savefile.default_directory": temp_dir,
            "download.default_directory": temp_dir,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True
        })
        chrome_options.add_argument("--kiosk-printing")

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )

        driver.get("https://graduacao.cesusc.edu.br/projetos/nucleo/uteis/login.php?&tid=0&lid=0&pid=24&arq_ret=R5QT1WSRQBMCVQVPFFQSF99MCT5RT44Q9WRW0RBM0FMM5QQ4R4CV59RWRF1F5SWCW0")
        wait = WebDriverWait(driver, 20)

        # Preenche login
        wait.until(EC.presence_of_element_located((By.NAME, "codigo"))).send_keys(usuario)
        wait.until(EC.presence_of_element_located((By.NAME, "senha"))).send_keys(senha)
        wait.until(EC.element_to_be_clickable((By.ID, "btn-entrar"))).click()

        time.sleep(2)

        # Clica em Notas e Frequências
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Notas e  Frequências')]"))).click()

        time.sleep(2)

        # Entra no iframe
        iframe = wait.until(EC.presence_of_element_located((By.ID, "iframe_conteudo")))
        driver.switch_to.frame(iframe)

        time.sleep(2)  # Tempo para carregar totalmente o conteúdo

        # Imprime com o navegador
        driver.execute_script("window.print();")
        time.sleep(2)  # Tempo para o PDF ser gerado

        # Procura PDF na pasta temporária
        lista_pdfs = glob.glob(os.path.join(temp_dir, "*.pdf"))
        if not lista_pdfs:
            raise Exception("Nenhum PDF foi gerado.")

        ultimo_pdf = max(lista_pdfs, key=os.path.getctime)
        nome_pdf_final = f"Notas_{usuario}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        caminho_final = os.path.join(pasta_destino, nome_pdf_final)

        shutil.move(ultimo_pdf, caminho_final)
        driver.quit()

        # Atualiza status e esconde gif
        def finalizar_sucesso():
            status_var.set("Finalizado com sucesso!")
            gif_label.pack_forget()
            if os.path.exists(caminho_final):
                os.startfile(caminho_final)
                messagebox.showinfo("Sucesso", f"✅ PDF salvo em:\n{caminho_final}")
            else:
                messagebox.showerror("Erro", "❌ PDF não foi movido corretamente.")
        janela.after(0, finalizar_sucesso)

    except Exception as e:
        def finalizar_erro():
            status_var.set("")
            gif_label.pack_forget()
            messagebox.showerror("Erro", f"Ocorreu um erro:\n{e}")
        janela.after(0, finalizar_erro)

def iniciar_execucao():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    if not usuario or not senha:
        messagebox.showwarning("Campos obrigatórios", "Preencha o usuário e a senha.")
        return

    pasta = filedialog.askdirectory(title="Escolha a pasta para salvar o PDF")
    if not pasta:
        messagebox.showwarning("Pasta não selecionada", "Por favor, selecione uma pasta.")
        return

    threading.Thread(target=rodar_script, args=(usuario, senha, pasta), daemon=True).start()

def alternar_senha():
    if entry_senha.cget('show') == '*':
        entry_senha.config(show='')
        btn_toggle.config(text='🙈')
    else:
        entry_senha.config(show='*')
        btn_toggle.config(text='👁️')

# ===== INTERFACE =====
janela = tk.Tk()
janela.title("Notas e Frequências - CESUSC")
janela.geometry("400x320")
janela.configure(bg="#f4f4f4")
janela.resizable(False, False)

# Centralizar janela
janela.update_idletasks()
largura = janela.winfo_width()
altura = janela.winfo_height()
x = (janela.winfo_screenwidth() // 2) - (largura // 2)
y = (janela.winfo_screenheight() // 2) - (altura // 2)
janela.geometry(f"{largura}x{altura}+{x}+{y}")

# Título
tk.Label(janela, text="Gerar PDF - CESUSC", font=("Helvetica", 16, "bold"), bg="#f4f4f4", fg="#333").pack(pady=10)

# Usuário
tk.Label(janela, text="Usuário (Matrícula):", bg="#f4f4f4", fg="#333").pack(pady=(10, 2))
entry_usuario = tk.Entry(janela, width=30)
entry_usuario.pack(pady=2)

# Senha
tk.Label(janela, text="Senha:", bg="#f4f4f4", fg="#333").pack(pady=(10, 2))
frame_senha = tk.Frame(janela, bg="#f4f4f4")
frame_senha.pack()
entry_senha = tk.Entry(frame_senha, width=27, show="*")
entry_senha.pack(side=tk.LEFT, padx=(0, 5))
btn_toggle = tk.Button(frame_senha, text="👁️", command=alternar_senha, width=2)
btn_toggle.pack(side=tk.LEFT)

# Botão Gerar
btn = tk.Button(
    janela,
    text="📄 Gerar PDF",
    command=iniciar_execucao,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 11),
    padx=20,
    pady=10
)
btn.pack(pady=15)

# Status (carregando...)
status_var = tk.StringVar()
label_status = tk.Label(janela, textvariable=status_var, font=("Arial", 10), bg="#f4f4f4", fg="gray")
label_status.pack()

# Caminho absoluto para o GIF na mesma pasta do script
caminho_gif = os.path.join(os.path.dirname(os.path.abspath(__file__)), "loading.gif")

# Carrega o GIF animado
try:
    gif_frames = carregar_gif_animado(caminho_gif)
except Exception as e:
    print(f"Erro ao carregar GIF: {e}")
    gif_frames = []

gif_label = tk.Label(janela, bg="#f4f4f4")
if gif_frames:
    animar_gif(gif_label, gif_frames)
    gif_label.pack_forget()  # começa escondido

janela.mainloop()
