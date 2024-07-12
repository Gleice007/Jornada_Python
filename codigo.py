"""
Passo 1 - entrar no sistema da empresa
    link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
Passo 2 - Fazer login
Passo 3 - Pegar/Importar a base de dados
Passo 4 - Cadastrar um produto
Passo 5 - Repetir o passo 4 até cadastrar todos os produtos
"""
import time
import pyautogui
#pyautogui.click - clicar com o mause
#pyautogui.write - escrever um texto
#pyautogui.press - aperta 1 tecla
#pyautogui.hotkey - combinação de teclas (ctrl C)
#pyautogui.scroll - rolar a tela para cima e para baixo
pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=-854, y=405)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("gleicielerodrigues57@gmail.com")
pyautogui.press("tab")
pyautogui.click(x=-797, y=564)

time.sleep(3)

import pandas

tabela = pandas.read_csv("produtos.csv")

print(tabela)
# para cada linha da minha tabela:

for linha in tabela.index:

    # codigo
    pyautogui.click(x=-840, y=290)
    
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)

    # marca
    pyautogui.press("tab")
    pyautogui.write("marca")

    # tipo
    pyautogui.press("tab")
    pyautogui.write("tipo")

    # categoria
    pyautogui.press("tab")
    pyautogui.write("categoria")

    # preço_unitario
    pyautogui.press("tab")
    pyautogui.write("preco")

    # custo
    pyautogui.press("tab")
    pyautogui.write("custo")

    # obsobs
    pyautogui.press("tab")
    pyautogui.write("obs")

    pyautogui.press("tab")  
    pyautogui.press("enter")
    
    pyautogui.scroll(1000)


