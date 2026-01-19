import pyautogui
import time

pyautogui.PAUSE = 1
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Passo 1: entrar no sistema da empresa
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
#fazer uma pausa maior para carregar o site
time.sleep(2)

# Passo 2: fazer login
# clicar no campo de e-mail
pyautogui.click(x=412, y=407)
pyautogui.write("fuentesbr@gmail.com")
pyautogui.press("tab") # passar para o próximo campo
pyautogui.write("joao")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2)

# Passo 3: abrir a base de dados (importar o arquivo)
import pandas

tabela = pandas.read_csv("produtos.csv") #vai ler as informações da base de dados
print(tabela)

# para cada linha da tabela (produto) eu preciso repetir o passo 4
for linha in tabela.index:
    # Passo 4: cadastrar 1 produto
    pyautogui.click(x=408, y=294)
    # código
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    # tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    # categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    # preço
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    # custo
    custo = str(tabela.loc[linha, "custo"])     
    pyautogui.write(custo)
    pyautogui.press("tab")
    # OBS
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")

    #depois que cadastrar todo o item precisa voltar para o início da tela.
    pyautogui.scroll(5000)