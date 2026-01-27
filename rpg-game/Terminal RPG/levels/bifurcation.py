import os
import sys
import time

import functions
from functions import clear, animated_text, color, lost_text, cura, combate, cor, text_oscilate
from classes import ladrao, guerreiro, piromante, feiticeiro
from classes import adaga, espada, machado, lanca
from classes import goblin, pocao_cura
import levels.level1

from levels.level1 import jogar_level1
from levels.caminho_baixo import jogar_caminho_baixo
from levels.caminho_reto import jogar_caminho_reto

def jogar_bifurcation():
    animated_text(
        '\nVocê segue adiante e encontra uma bifurcação...\n'
    )
    animated_text(
        color(
            'Você quer ir para direita ou para a esquerda: \n\n', cor.blue
        )
    )
    while True:
        animated_text(color('[1]Esquerda\n[2]Direita',cor.blue))
        decisao = int(input(animated_text(color('\n\nResposta: ',cor.red))))
        

        if decisao == 1:
            jogar_caminho_baixo()
            break
        elif decisao == 2:
            jogar_caminho_reto()
            break
        else:
            print("Decisão invalida. Tente novamente.")