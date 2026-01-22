import os
import sys
import time

from functions import clear, animated_text, color, lost_text, cura, combate, cor
from classes import ladrao, guerreiro, piromante, feiticeiro
from classes import adaga, espada, machado, lanca
from classes import goblin, pocao_cura
import levels.level1

from levels.level1 import jogar_level1
from levels.caminho_baixo import jogar_caminho_baixo


clear()

def main():
    #jogar_level1()

    animated_text(
        '\nVocê segue adiante e encontra uma bifurcação...\n'
    )
    animated_text(
        color(
            'Você quer ir para direita ou para a esquerda: \n\n', cor.blue
        )
    )
    decisao = int(input('[1]Esquerda\n[2]Direita'))

    



     



if __name__ == "__main__":
    main()


