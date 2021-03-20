# Importa libs 
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


lista_de_contas = list()
quant_vesez_comentado = 0
index_conta = 0


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
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.instagram.com/')
    sleep(5)

    ## username
    campo_username = driver.find_element_by_xpath("//input[@name='username']")
    campo_username.click()
    campo_username.clear()
    campo_username.send_keys(email)

    ## password
    campo_password = driver.find_element_by_xpath("//input[@name='password']")
    campo_password.click()
    campo_password.clear()
    campo_password.send_keys(senha)
    campo_password.send_keys(Keys.RETURN)
    print(f'\033[32mUsando a conta {lista_de_contas[index_conta][0]}, com comentarios na intervalo de {tempo[0]} a {tempo[1]} segundos\033[m')
    sleep(5)
    comentarFoto(driver, foto)
    return driver


def digitar_como_uma_pessoa(frase, onde_digitar):
    for letra in frase:
        onde_digitar.send_keys(letra)
        sleep(random.randint(1,5)/30)


# Comentar na foto
def comentarFoto(driver, foto):
    global index_conta
    i = 0

    # Entarando na foto
    driver.get(f'https://www.instagram.com/p/{foto}/')
    sleep(2)
    print('\033[32mEntrou na foto com sucesso\033[m')

    # Comentar
    while True:
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
                campo_comentar.send_keys(Keys.RETURN)
                sleep(random.randint(tempo[0],tempo[1]))
                print('\033[32mComentando...\033[m')

                # publicar

                i += 1
                print(i)
        except:
            print(f'{i} comentarios')
            print('\033[31mSua conta foi bloqueada\033[m \033[34m Trocando de conta\033[m')

        # Fechar aba e aumentar o index da lista conta
        index_conta += 1
        driver.quit()
        sleep(2)

        # Se as conta acabar ele vai zerar o indedx e começar da primeira conta
        if index_conta == len(lista_de_contas):
            index_conta = 0
            sleep(2)

        print(index_conta)
        login(lista_de_contas[index_conta][0], lista_de_contas[index_conta][1])
        

# Colocando as  contas do insta num arquivo
with open("lista_contas.txt", "r+") as contas:
        for conta in contas:
            conta = conta.split(':')
            lista_de_contas.append(conta.copy())


print('''
[ 1 ] - configuração padrão
[ 2 ] - personalizar
''')

op = 1

if op == 1:
    username = lista_de_contas[0][0]
    password = lista_de_contas[0][1]
    tempo = [60, 70]
    foto = 'CMkHfHGFcZR'
    quant_amigos_marca = 2
else:
    tempo = list()
    username = input('Email: ')
    password = input('Senha: ')
    foto = input('Foto: ')
    tempo.append(int(input('De: ')))
    tempo.clear()
    tempo.append(int(input('A: ')))
    quant_amigos_marca = input('Quantos amigos marca: ')


driver = login(username, password)
