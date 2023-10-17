from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


user = 'alex.santos'
passw = 'wWytK5goh@'

def definicao_username_senha():
    import customtkinter as CTk
    import pyautogui

    def coletar_dados():
        global user, passw

        user = username_entry.get()
        passw = password_entry.get()

        root.destroy()

    def destroy():
        root.destroy()

    def centralizar(janela):
        # dimensoes
        largura = 300
        altura = 300

        # resulução do sistema
        width, height = pyautogui.size()
        print(f"height: {height} x Width: {width}")

        # posicao da tela
        posix = (width // 2) - 150
        posiy = (height // 2) - 150
        print(f"posix: {posix} x posiy: {posiy}")

        # definir a geometry
        janela.geometry(f"{largura}x{altura}+{posix}+{posiy}")
    

    root = CTk.CTk()
    root.title("Usuario/senha")
    centralizar(root)
    root.resizable(False, False)

    # Criar um campo com username

    username_label = CTk.CTkLabel(root, text="Username")
    username_entry = CTk.CTkEntry(root)

    # Criar um campo com senha

    password_label = CTk.CTkLabel(root, text="Senha")
    password_entry = CTk.CTkEntry(root, show="*")

    # Cria um botão para seguir

    button = CTk.CTkButton(root, text="Seguir", command=coletar_dados)

    button_2 = CTk.CTkButton(root, text="Pular", command=destroy)

    # Adicionar os widgets à janela

    username_label.pack(padx=10, pady=10)
    username_entry.pack(fill="x", expand=True, padx=10, pady=10)
    password_label.pack(padx=10, pady=10)
    password_entry.pack(fill="x", expand=True, padx=10, pady=10)
    button.pack(padx=10, pady=10)
    button_2.pack(padx=10, pady=10)

    root.mainloop()


definicao_username_senha()   

driver = webdriver.Chrome()

driver.get(r"https://srv-zbx-01.fhptelecom.com.br/index.php")

name = driver.find_element(By.ID, "name")
name.send_keys(user)

password = driver.find_element(By.ID, "password")
password.send_keys(passw)

sign_in = driver.find_element(By.ID, "enter")
sign_in.click()

driver.get(r"https://srv-zbx-01.fhptelecom.com.br/zabbix.php?action=dashboard.view&dashboardid=50")

driver.fullscreen_window()

input()