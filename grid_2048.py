import random as rd
from game2048.textual_2048 import *

THEMES = {"0": {"name": "Default", 0: "", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}


def grid_get_value(grid,i,j):
    return grid[i][j]


def create_grid(n):
    game_grid = []
    for i in range(0,n):
        game_grid.append([0]*n)
    return game_grid


def get_value_new_tile():
    n = rd.randint(1,10)
    if n >= 2 :
        return 2
    else :
        return 4


def get_all_tiles(grid):
    tiles = []

    for ligne in grid :
        for c in ligne :
            x = c
            if c == ' ':
                x = 0
            tiles.append(x)
    return tiles


def get_empty_tiles_positions(grid):
    n = len(grid)
    empty_tiles = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] in [' ',0] :
                empty_tiles.append((i,j))
    return empty_tiles


def get_new_position(grid):
    empty_tiles = get_empty_tiles_positions(grid)
    a, b = rd.choice(empty_tiles)
    grid[a][b] = 0
    return a, b


def grid_add_new_tile(grid):
    a,b = get_new_position(grid)
    x = get_value_new_tile()
    grid[a][b] = x
    return grid


def init_game(n):
    grid = create_grid(n)
    grid = grid_add_new_tile(grid)
    grid = grid_add_new_tile(grid)

    return grid


def grid_to_string_with_size(grid, n):
    taille_max = len(str(max([max(l) for l in grid])))

    affichage = (' ' + '='*taille_max)*n + '\n'


    for i in range(n) :
        for j in range(n) :
            affichage += '|' + ' '*(taille_max - len(str(grid[i][j]))) + str(grid[i][j])
        affichage += '|\n'+(' ' + '='*taille_max)*n + '\n'


    return affichage


def long_value(grid):
    return len(str(max([max(l) for l in grid])))


grid = [[256,0,2048],[0,2,4],[0,0,0]]


def long_value_with_theme(grid, theme):
    max = 0
    n = len(grid)

    for i in range(n):
        for j in range(n):
            a = len(str(THEMES[theme][grid[i][j]]))
            if a > max :
                max = a
    return max


def grid_to_string_with_size_and_theme(grid,theme,taille_max):
    n = len(grid)
    affichage = (' ' + '='*taille_max)*n + '\n'


    for i in range(n) :
        for j in range(n) :
            affichage += '|' + ' '*(taille_max - len(str(THEMES[theme][grid[i][j]]))) + str(THEMES[theme][grid[i][j]])
        affichage += '|\n'+(' ' + '='*taille_max)*n + '\n'


    return affichage

def move_row_left(row):
    n = len(row)
    liste = []
    for k in range(1,n):
        i = k
        while i > 0:
            if row[i-1] == 0:
                row[i-1], row[i] = row[i], 0

            elif row[i-1] == row[i] and not (i-1) in liste:
                row[i-1], row[i] = 2*row[i], 0
                liste.append(i-1)
                break
            i -= 1

    return row

row = [2, 2, 2, 2]

def rev(liste):
    n = len(liste)
    a = [0]*n

    for i in range(n):
        a[n-i-1] = liste[i]

    return a


def move_row_right(row):
    return rev(move_row_left(rev(row)))

def transpose(grid):
    n = len(grid)
    a = grid
    for i in range(n):
        for j in range(i+1,n):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    return a

def pivote(grid):
    n = len(grid)
    a = [[0]*n for i in range(n)]

    for i in range(n):
        for j in range(n):
            a[i][j] = grid[j][n-i-1]

    return a


def move_grid(grid, d):
    b = grid
    if d == 'g':
        b = [move_row_left(row) for row in grid]
    if d == 'd':
        b = [move_row_right(row) for row in grid]
    if d == 'h':
        a = pivote(grid)
        b = pivote(pivote(pivote([move_row_left(row) for row in a])))
    if d == 'b':
        a = pivote(grid)
        b = pivote(pivote(pivote([move_row_right(row) for row in a])))
    return b


a = [[0,0,0],[0,0,0],[0,0,1]]


def is_full(grid):
    n = len(grid)

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                return False

    return True


def move_possible(grid):
    liste_mouvements = ['g','d','h','b']
    for i in range(4):
        liste_mouvements[i] = not (grid == move_grid(grid, liste_mouvements[i]))
    return liste_mouvements


def is_game_over(grid):
    liste_mouvements = move_possible(grid)
    return not (True in liste_mouvements)


def get_grid_tile_max(grid):
    max = 0
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] > max:
                max = grid[i][j]
    return max


def is_won(grid):
    return get_grid_tile_max(grid) >= 2048


def random_play(theme):
    grid = init_game(4)
    move = ['g','d','h','b']
    while not is_game_over(grid):
        grid = move_grid(grid,rd.choice(move))
        print(grid_to_string_with_size_and_theme(grid,theme,long_value_with_theme(grid, theme)))
        print("\n")
        if not is_full(grid):
            grid = grid_add_new_tile(grid)
            print(grid_to_string_with_size_and_theme(grid,theme,long_value_with_theme(grid, theme)))
        print("\n")
        if get_grid_tile_max(grid) >= 2048:
            Score = sum([sum(l) for l in grid])
            print("You won")
            print("Score :")
            print(Score)

    Score = sum([sum(l) for l in grid])
    print("You lost")
    print("Score :")
    print(Score)


def game_play():
    size = int(read_size_grid())
    theme = read_theme_grid()
    grid = init_game(size)

    while not is_game_over(grid):
        move = read_player_command()
        grid = move_grid(grid,move)
        print(grid_to_string_with_size_and_theme(grid,theme,long_value_with_theme(grid, theme)))
        print("\n")
        if not is_full(grid):
            grid = grid_add_new_tile(grid)
            print(grid_to_string_with_size_and_theme(grid,theme,long_value_with_theme(grid, theme)))
        print("\n")
        if get_grid_tile_max(grid) >= 2048:
            Score = sum([sum(l) for l in grid])
            print("You won")
            print("Score :")
            print(Score)

    Score = sum([sum(l) for l in grid])
    print("You lost")
    print("Score :")
    print(Score)


grid=[[16, 4, 8, 2], [2, 4, 2, 128], [4, 512, 32, 64], [1024, 2048, 512, 2]]
print(grid_to_string_with_size_and_theme(grid,"1",4))



































