import os
import sys
import time

from functions import clear, animated_text, color, lost_text, cura, combate, cor
from classes import ladrao, guerreiro, piromante, feiticeiro
from classes import adaga, espada, machado, lanca
from classes import goblin, pocao_cura
from functions import text_oscilate
import levels.level1

from levels.level1 import jogar_level1
from levels.caminho_baixo import jogar_caminho_baixo
from levels.caminho_reto import jogar_caminho_reto
from levels.bifurcation import jogar_bifurcation
from transition_level import jogar_bifurcation_transition


clear()

def main():
    #jogar_level1()

    #jogar_bifurcation()

    jogar_bifurcation_transition()

    



     



if __name__ == "__main__":
    main()


