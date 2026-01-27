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

def text_oscilate(texto, vezes=10, intervalo=0.3):
    print('\n')

    for _ in range(vezes):
        sys.stdout.write("\r" + texto)
        sys.stdout.flush()
        time.sleep(intervalo)

        sys.stdout.write("\r" + " " * len(texto))
        sys.stdout.flush()
        time.sleep(intervalo)
    print()

def lost_text():
    text_error = (color('===================VOCÊ PERDEU==================\n\n', cor.redbg))
    animated_text(text_error)
    time.sleep(1)

def cura(jogador, quantidade):
    jogador.vida += quantidade
    if jogador.vida > jogador.vida_max:
        jogador.vida = jogador.vida_max

def combate(jogador, inimigo):
    clear()
    print(color('⚔️ COMBATE INICIADO ⚔️\n', cor.red))

    while jogador.vida > 0 and inimigo.vida > 0:
        jogador.status()
        inimigo.status()

        print('\n[1] Atacar')
        print('[2] Fugir')

        escolha = input('\nO que você faz? ')

        if escolha == '1':
            jogador.atacar(inimigo)

            if inimigo.vida <= 0:
                print(color('\nVocê derrotou o inimigo!\n', cor.green))
                break

            time.sleep(1)
            inimigo.atacar(jogador)

            if jogador.vida <= 0:
                lost_text()
                sys.exit()

        elif escolha == '2':
            batlle_text_defeat = print(color('\nVocê tentou fugir, mas o inimigo te alcançou!\n', cor.red))
            animated_text(batlle_text_defeat)
            lost_text()
            inimigo.atacar(jogador)
            break

        time.sleep(2)
        clear()

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