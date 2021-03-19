# Importa libs 
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


def login(email, senha):
    sleep(5)

    ## usename
    username = driver.find_element_by_name('username')
    username.click()
    username.clear()
    username.send_keys(email)

    ## password
    password = driver.find_element_by_name('password')
    password.click()
    password.clear()
    password.send_keys(senha)
    password.send_keys(Keys.RETURN)
    sleep(5)


def digitar_como_uma_pessoa(frase, onde_digitar):
    for letra in frase:
        onde_digitar.send_keys(letra)
        sleep(random.randint(1,5)/30)


# Comentar na foto
def comentarFoto(foto):

    # Entarando na foto
    driver.get(f'https://www.instagram.com/p/{foto}/')
    sleep(2)
    print('\033[32mEntrou na foto com sucesso\033[m')

    # Comentar
    i = 0
    while True:
        try:
            with open('amigos.txt', 'a+') as amigos:
                comentarios = ['teste']
            driver.find_element_by_class_name('Ypffh').click()
            campo_comentar = driver.find_element_by_class_name('Ypffh')
            sleep(random.randint(1, 5))
            digitar_como_uma_pessoa(random.choice(comentarios), campo_comentar)
            sleep(random.randint(tempo[0],tempo[1]))
            print('\033[32mComentando...\033[m')
            i += 1
        except :
            print(i + 'Coomentarios')


# login(email, senha)
# comentarFoto(foto)

class BotSorteio():
    def __init__(self, username, password):
        self.username = input('Email: ')
        self.password = input('Senha: ')
        self.driver = driver = webdriver.Chrome(ChromeDriverManager().install())

    def login(self):
        # Entrando no Instagram
        driver = self.driver
        driver.get('https://www.instagram.com/')


        campo_username = driver.find_element_by_name('username')
        campo_username.click()
        campo_username.clear()
        campo_username.send_keys(self.username)

        ## password
        campo_password = driver.find_element_by_name('password')
        campo_password.click()
        campo_password.clear()
        campo_password.send_keys(self.password)
        campo_password.send_keys(Keys.RETURN)

    def digitar_como_uma_pessoa(frase, onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            sleep(random.randint(1,5)/30)


    # Comentar na foto
    def comentarFoto(self, foto):

        # Entarando na foto
        self.driver.get(f'https://www.instagram.com/p/{foto}/')
        sleep(2)
        print('\033[32mEntrou na foto com sucesso\033[m')

        # Comentar
        i = 0
        while True:
            try:
                with open('amigos.txt', 'a+') as amigos:
                    comentarios = ['teste']
                self.driver.find_element_by_class_name('Ypffh').click()
                campo_comentar = driver.find_element_by_class_name('Ypffh')
                sleep(random.randint(1, 5))
                digitar_como_uma_pessoa(random.choice(comentarios), campo_comentar)
                sleep(random.randint(tempo[0],tempo[1]))
                print('\033[32mComentando...\033[m')
                i += 1
            except :
                print(i + 'Coomentarios')



print('''
[ 1 ] - configuração padrão
[ 2 ] - personalizar
''')
op = input('Qual sua opção: ')

if op != 1:
    username = 'luisj2felipe09@gmail.com'
    password = 'Luis9090'
    tempo = [1, 5]
    foto = 'CMkgtgIlVNt'
    print(f'\033[32mUsando a conta {username}, com comentarios na intervalo de 60 a 70 segundos\033[m')
else:
    tempo = list()
    username = input('Email: ')
    password = input('Senha: ')
    foto = input('Foto: ')
    tempo.append(input('De: '))
    tempo.clear()
    tempo.append(input('A: '))

BotSorteio(username, password)
BotSorteio.login()