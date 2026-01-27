import sys
import time

from functions import clear, animated_text, color, lost_text, cura, combate, cor
from classes import (
    ladrao, guerreiro, piromante, feiticeiro,
    adaga, espada, machado, lanca,
    Jogador, goblin, pocao_cura
)


def jogar_level1():
    clear()
    chave = False

    nome_usuario = input('Digite seu nome: ')
    clear()

    print('======== Seja Bem-vindo', nome_usuario, '========')

    print(color('[1] Feiticeiro          ', cor.purple), color('[2] Guerreiro', cor.blue))
    print(color('[3] Ladrão              ', cor.cyan),   color('[4] Piromante', cor.green))

    classe_escolhida = int(input('Qual classe você deseja jogar?: '))

    if classe_escolhida == 1:
        classe = feiticeiro
    elif classe_escolhida == 2:
        classe = guerreiro
    elif classe_escolhida == 3:
        classe = ladrao
    elif classe_escolhida == 4:
        classe = piromante
    else:
        animated_text(color('Classe inválida!', cor.red))
        sys.exit()

    clear()

    animated_text(
        'Você acorda em uma cela, junto a você só há o esqueleto de outro prisioneiro...\n\n'
    )

    acao1 = int(input('Pegar chave?\n[1] Sim\n[2] Não\n\nResposta: '))

    if acao1 != 1:
        animated_text(color('Tu é burro mermão, tu acha mesmo que tu tem escapatoria daqui...............\n',cor.red))
        lost_text()
        sys.exit()

    chave = True
    animated_text(color('==== Você pegou a chave ====\n', cor.green))

    animated_text(
        'Você sai da cela e vê um soldado caído no chão.\n'
        'Você quer pegar a arma dele?\n\n'
    )

    acao2 = int(input('[1] Sim\n[2] Não\n\nResposta: '))

    if acao2 != 1:
        animated_text(color('Você tenta seguir, mas logo a frente é surpreendido por um goblin, que sedento de sangue, te estupra violentamente',cor.red))
        sys.exit()

    if classe == ladrao:
        arma = adaga
    elif classe == guerreiro:
        arma = espada
    elif classe == piromante:
        arma = machado
    else:
        arma = lanca

    animated_text(color(f'Você pegou a {arma.nome}!\n', cor.green))


    animated_text(color('\nUm goblin aparece!\n', cor.red))
    acao3 = input(
        color(
            'Você deseja fugir ou lutar\n\n[1]Fugir\n[2]Lutar\n\nResposta: ',cor.red
        )
    )
    if acao3 != 1:
        animated_text(
            color(
                'PREPARESSE', cor.bluebg
            )
        )
        player = Jogador(nome_usuario, classe, arma)
    else:
        animated_text(
            color(
                'Viadinho', cor.red
            )
        )
        lost_text()
        sys.exit()
        clear()

    combate(player, goblin)


    animated_text(
        color(
            '\nDepois dessa batalha, você anda mais um pouco e acha um mistorioso frasco com um liquido brialhante\n',
            cor.green
        )
    )

    acao4 = animated_text(input('[1] Beber\n[2] Não beber\n\nResposta: '))

    if acao4 == 1:
        cura(player, pocao_cura)
        if player.vida < player.vida_max:
            animated_text(
                color(
                    '\nVocê bebe o liquido, mas já está com a vida cheia, nada acontece.\n\n', cor.brown
                )
            )
    else:
        animated_text(
            color(
                '\nVocê bebe o liquido e sente uma energia revigorante percorrer seu corpo, sua vida foi restaurada em 20 pontos!\n\n', cor.green
                )
            )
        print(color(f'Sua vida atual é: {player.vida} | {player.vida_max}', cor.cyan))
        time.sleep(3)
        clear()
