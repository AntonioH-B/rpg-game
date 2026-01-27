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

class Jogador:
    def __init__(self, nome, classe, arma):
        self.nome = nome
        self.classe = classe.nome
        self.vida = classe.vida
        self.vida_max = classe.vida
        self.forca = classe.forca
        self.resistencia = classe.resistencia
        self.inteligencia = classe.inteligencia
        self.arma = arma

    def atacar(self, inimigo):
        dano_total = self.forca + self.arma.dano
        inimigo.vida -= dano_total
        print(f'\n{self.nome} atacou {inimigo.nome} e causou {dano_total} de dano!')

    def status(self):
        print(f'\n{self.nome} | Vida: {self.vida} | {self.vida_max}')
    
class Inimigo:
    def __init__(self, nome, vida, dano, velocidade):
        self.nome = nome
        self.vida = vida
        self.vida_max = vida
        self.dano = dano
        self.velocidade = velocidade

    def atacar(self, jogador):
        jogador.vida -= self.dano
        print(f'{self.nome} atacou {jogador.nome} causando {self.dano} de dano!')

    def status(self):
        print(f'{self.nome} | Vida: {self.vida} | {self.vida_max}')

pocao_cura = 20

goblin = Inimigo(
    nome='Goblin',
    vida=60,
    dano=10,
    velocidade=12
)