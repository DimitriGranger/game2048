from game2048.grid_2048 import *


def read_player_command():
    move = 0
    while not move in ['g','d','h','b'] :
        move = input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")

    return move


def read_size_grid():
    size = input("Entrez la taille de grille voulue.")

    return size


def read_theme_grid():
    theme = input("Entrez le thème voulu.")

    while not theme in ['0','1','2']:
        theme = input("Entrez le thème voulu.")

    return theme


if __name__ == '__main__':
    game_play()
    exit(1)






