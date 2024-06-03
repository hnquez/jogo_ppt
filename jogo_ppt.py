#objetivo: criar um jogo de pedra papel e tesoura, e no final toca uma musica de vitoria
import random
import pygame
print('Vamos jogar pedra, papel e tesoura!')
usuario = str(input('Sua vez: ')) #pede ao usuario para escolher
opcoes = ['pedra', 'papel', 'tesoura'] #lista das opcoes para o pc
pc = random.choice(opcoes)
if usuario == 'pedra' and pc == 'papel':
    print('Você escolheu {} e eu {}, voce perdeu'.format(usuario, pc))
elif usuario == 'papel' and pc == 'tesoura':
    print('Você escolheu {} e eu {} voce perdeu'.format(usuario, pc))
elif usuario == 'tesoura' and pc == 'papel':
    print('')