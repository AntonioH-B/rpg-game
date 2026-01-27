import os
import sys
import time

from functions import clear, animated_text, color, lost_text, cura, combate, cor
from classes import ladrao, guerreiro, piromante, feiticeiro
from classes import adaga, espada, machado, lanca
from classes import goblin, pocao_cura
import levels.level1
from transition_level.bifurcation_transition import jogar_bifurcation_transition

def jogar_caminho_baixo():
    animated_text(color('Você decide seguir pelo caminho da esquerda, você chega no fim do tunel, e se depara com uma imensa escadaria, que se extende por varios metros\n\n',cor.green))
    animated_text(color('Você quer continuar ou voltar\n\n[1]Voltar\n[2]Continuar\n\n'))
    decisao = int(input((animated_text('Resposta: '))))

    if decisao == 1:
        jogar_bifurcation_transition()
    elif decisao == 2:
        animated_text(color('Você segue descendo as escadas por muito tempo, a fome, sede e dor acabam com você, até que você chega numa sala enorme com com grande goblind no centro dela....',cor.red))

    animated_text(color('O que você faz: \n\n[1]Lutar\n[2]Fugir\n\n'))
    decisao1 = int(input(animated_text('Reposta: ',cor.bluebg)))

    if decisao1 == 1:
        combate()
    elif decisao1 == 2:
        lost_text()
        animated_text(color('Tu realmente achou que ia fugir da merda dum goblin enorme, kkkkkkkkkkkkkkkkkkkkkkkk'))
        time.sleep(5)
        sys.exit()
        clear()