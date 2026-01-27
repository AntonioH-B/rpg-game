import os
import sys
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def color(a, b):
    return b + str(a) + cor.closed

def animated_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def lost_text():
    text_error = (color('===================VOCÊ PERDEU==================\n\n', cor.redbg))
    animated_text(text_error)
    time.sleep(1)
    
class Inimigo:
    def __init__(self, nome, vida, dano, velocidade):
        self.nome = nome
        self.vida = vida
        self.dano = dano
        self.velocidade = velocidade

    # Método para atacar
    def atacar(self, alvo):
        print(f'{self.nome} atacou {alvo} causando {self.dano} de dano!')
        # Aqui você poderia subtrair da vida do alvo, se fosse um objeto jogador

    # Método para mostrar status
    def status(self):
        print(f'{self.nome}: {self.vida} de vida, {self.dano} de dano, {self.velocidade} de velocidade')


class cor:
    blackbg = "\033[0;40m"
    redbg = "\033[0;41m"
    greenbg = "\033[0;42m"
    bluebg = "\033[0;44m"

    black = "\033[0;30m"
    red = "\033[0;31m"
    green = "\033[0;32m"
    brown = "\033[0;33m"
    blue = "\033[0;34m"
    purple = "\033[0;35m"
    cyan = "\033[0;36m"
    closed = '\033[m'
    n = ''

velocidade = 0
vida = 0
forca = 0
resistencia = 0
inteligencia = 0
dano = 0
chave = False
arma_no_chao = None

class ladrao: 
    nome = 'ladrao'
    vida = 90
    forca = 9
    resistencia = 10
    inteligencia = 12
class piromante: 
    nome = 'piromante'
    vida = 100
    forca = 12
    resistencia = 12
    inteligencia = 1
class feiticeiro: 
    nome = 'feiticeiro'
    vida = 80
    forca = 9
    resistencia = 8
    inteligencia = 15
class guerreiro: 
    nome = 'guerreiro'
    vida = 110
    forca = 13
    resistencia = 11
    inteligencia = 9
class machado:
    nome = 'machado'
    dano = 20
    velocidade = 10
class espada:
    nome = 'espada'
    dano = 15
    velocidade = 15
class adaga:
    nome = 'adaga'
    dano = 13
    velocidade = 20
class lanca:
    nome = 'lança'
    dano = 15
    velocidade = 13



vida, classe = 0, ''

clear()

nome_usuario = input('Digite seu nome: ')
clear()

print('========Seja Bem-vindo', nome_usuario,'==========')

cont = 1 
for cont in range(0,1):

    print(color('[1].feiticeiro          ', cor.purple),color('[2].guerreiro', cor.blue))
    print(color('[3].ladrao      ', cor.cyan),color('[4].piromante', cor.green))
    classe = int(input('Qual classe você deseja jogar?: '))

    if classe == 3:
        classe = ladrao
        cont = 0
    elif classe == 4:
        classe = piromante
        cont = 0
    elif classe == 2:
        cont = 0
        classe = guerreiro
    elif classe == 1:
        cont = 0
        classe = feiticeiro
    elif classe not in [1, 2, 3, 4]:
        animated_text(color('====Classe inválida, tente novamente====', cor.red))
        time.sleep(3)
        clear()
        sys.exit()
    else: 
        cont = 1


clear()

text1 = 'Você acorda em uma cela, junto a você só a o esqueleto de outro prisioneiro.\n\nVocê olha para grade da cela e enxerga um homem querendo te da uma chave...\n\n\n\n\n'
animated_text(text1)

text2 = 'Estranho: pegue aqui nobre guerreiro, pegue essa chave e nos salve'
animated_text(text2)
time.sleep(2)

clear()
while True:

    acao1 = int(input('pegar chave \n[1]sim \n[2]não\n\nResposta: '))
    if acao1 == 1:
        text3 = (color('====Você pegou a chave====', cor.green))
        chave = True
        animated_text(text3)
        break
    elif acao1 == 2:
        text4 = ('Você perdeu a oportunidade de sair da cela\n')
        animated_text(text4)
        lost_text()
        text_5 = (color('Um anão te estuprou até a morte kkkkkkk', cor.red))
        animated_text(text_5)
        time.sleep(5)
        break
clear()

if chave == True:
    clear()
    text6 = ('Você sai da cela e vê um soldado caído no chão, ele parece estar ferido.\n\nVocê quer pegar a arma dele?\n\n')
    animated_text(text6)

    acao2 = int(input('Pegar arma: \n[1]sim \n[2]não\n\nResposta: '))
    time.sleep(1)

    if acao2 == 1:
        if classe == ladrao:
            arma_no_chao = adaga
        elif classe == guerreiro:
            arma_no_chao = espada
        elif classe == piromante:
            arma_no_chao = machado
        elif classe == feiticeiro:
            arma_no_chao = lanca

        text7 = color(f'====Você pegou a {arma_no_chao.nome}!!! do soldado====', cor.green)
        animated_text(text7)
        time.sleep(3)
        clear()

    elif acao2 == 2:
        text8 = color('\nVocê tenta continuar sua jornada com as mãos vazias, mas acaba sendo pego por guardas e executado.\n\n', cor.red)
        text9 = color('===================VOCÊ PERDEU==================', cor.red)
        animated_text(text8)
        animated_text(text9)
        time.sleep(5)
        sys.exit()

    clear()

    text10 = color(f'Você pega a {arma_no_chao.nome} e segue em frente pela masmorra.\n\n', cor.blue)
    animated_text(text10)

    text11 = color('De repente, um goblin aparece na sua frente querendo te atacar!\n\n', cor.red)
    animated_text(text11)   

    text12 = color('Você decide fugir ou lutar?\n\n', cor.redbg)
    animated_text(text12)

    acao3 = int(input('Fugir ou lutar: \n[1]Fugir \n[2]Lutar\n\nResposta: '))
    if acao3 == 1:
        text13 = color('\nVocê tenta fugir, mas o goblin é mais rápido e te alcança, te matando sem piedade.\n\n', cor.red)
        animated_text(text13)
        lost_text()
        time.sleep(5)
        sys.exit()
        clear()
    elif acao3 == 2:
        print('hellor word!')
        sys.exit()

