# Importa libs 
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


index_conta = 0

def trocarConta():
    global index_conta
    index_conta += 1

    if index_conta == len(lista_de_contas):
        print('Suas contas acabou, voltando para a primeira conta!')
        index_conta = 0

    login(lista_de_contas[index_conta][0], lista_de_contas[index_conta][1])


def marcaAmigos(quant):
    pessoa_aleatoria = ''
    marcar = ''
    amigos = list()

    with open('amigos.txt', 'r+') as lista_amigos:
        for a in lista_amigos:
            amigos.append(a)

        for e, x in enumerate(range(0, quant)):
            pessoa_aleatoria = random.choice(amigos).replace('\n', ' ')

            if e == 0:
                marcar += pessoa_aleatoria
            else:
                while pessoa_aleatoria in marcar:
                    pessoa_aleatoria = random.choice(amigos).replace('\n', ' ')

                marcar += pessoa_aleatoria
            
    return marcar


def login(email, senha):
    # Entrando no Instagram
    driver = webdriver.Chrome('chromedriver')
    driver.get('https://www.instagram.com/')
    sleep(10)

    ## username
    campo_username = driver.find_element(By.CSS_SELECTOR, "[name='username']")
    campo_username.click()
    campo_username.clear()
    campo_username.send_keys(email)

    ## password
    campo_password = driver.find_element(By.CSS_SELECTOR, "[name='password']")
    campo_password.click()
    campo_password.clear()
    campo_password.send_keys(senha)
    campo_password.send_keys(Keys.RETURN)
    print(f'\033[32mUsando a conta {email}, com comentarios na intervalo de {tempo[0]} a {tempo[1]} segundos\033[m')
    sleep(10)
    comentarFoto(driver, foto)
    return driver


def digitar_como_uma_pessoa(frase, onde_digitar):
    for letra in frase:
        onde_digitar.send_keys(letra)
        sleep(random.randint(1,5)/30)


# Comentar na foto
def comentarFoto(driver, foto):
    quant_comentarios = 0

    # Entarando na foto
    driver.get(foto)
    sleep(5)
    print('\033[32mEntrou na foto com sucesso\033[m')

    # Comentar
    try:
        while True:
            # lista de cometários
            comentarios = marcaAmigos(quant_amigos_marca)

            # clicando no campo comtentário
            driver.find_element_by_class_name('Ypffh').click()
            campo_comentar = driver.find_element_by_class_name('Ypffh')
            sleep(random.randint(1, 5))

            # digitando um comentário aleatorio
            digitar_como_uma_pessoa(comentarios, campo_comentar)
            sleep(5)
            # publicar

            campo_comentar.send_keys(Keys.RETURN)
            sleep(random.randint(tempo[0],tempo[1]))
            print('\033[32mComentando...\033[m')

            quant_comentarios += 1
            print(quant_comentarios)
    except Exception as erro:
        print(erro)
        print(f'{quant_comentarios} comentarios')
        print('[31mSua conta foi bloqueada\033[m \033[34m Trocando de conta')

        driver.quit()
        sleep(5)

        trocarConta()


lista_de_contas = list()
# Colocando as  contas do insta num arquivo
with open("lista_contas.txt", "r+") as contas:
        for conta in contas:
            conta = conta.split(':')
            lista_de_contas.append(conta.copy())

# Parte que pode mexer

# =================================================

op = 1

if op == 1:
    username = lista_de_contas[0][0]
    password = lista_de_contas[0][1]
    tempo = [5 , 2]
    foto = 'https://www.instagram.com/p/CNviRv3rUC0/'
    quant_amigos_marca = 2


# =================================================

driver = login(username, password)
