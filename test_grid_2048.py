from game2048.grid_2048 import *


def test_get_value_new_tile():
    assert get_value_new_tile()== 2 or 4


def test_get_all_tiles():
    assert get_all_tiles( [[' ',4,8,2], [' ',' ',' ',' '], [' ',512,32,64], [1024,2048,512, ' ']]) == [0,4,8,2,0,0,0,0,0,512,32,64, 1024,2048,512,0]
    assert get_all_tiles([[16,4,8,2], [2,4,2,128], [4,512,32,64], [1024,2048,512,2]]) == [16, 4, 8, 2, 2, 4, 2, 128, 4, 512, 32, 64, 1024, 2048, 512, 2]
    assert get_all_tiles(create_grid(3))== [0 for i in range(9)]

def test_get_empty_tiles_positions():
    assert get_empty_tiles_positions([[0, 16, 32, 0], [64, 0, 32, 2], [2, 2, 8, 4], [512, 8, 16, 0]])==[(0,0),(0,3),(1,1),(3,3)]
    assert get_empty_tiles_positions([[' ', 16, 32, 0], [64, 0, 32, 2], [2, 2, 8, 4], [512, 8, 16, 0]])==[(0,0),(0,3),(1,1),(3,3)]
    assert get_empty_tiles_positions(create_grid(2))==[(0,0),(0,1),(1,0),(1,1)]
    assert get_empty_tiles_positions([[16,4,8,2], [2,4,2,128], [4,512,32,64], [1024,2048,512,2]])==[]

def test_init_game():
    grid = init_game(4)
    tiles = get_all_tiles(grid)
    assert 2 or 4 in tiles
    assert len(get_empty_tiles_positions(grid)) == 14




def test_get_new_position():
    grid = [[0, 16, 32, 0], [64, 0, 32, 2], [2, 2, 8, 4], [512, 8, 16, 0]]
    x,y=get_new_position(grid)
    assert(grid_get_value(grid,x,y)) == 0
    grid = [[' ',4,8,2], [' ',' ',' ',' '], [' ',512,32,64], [1024,2048,512, ' ']]
    x,y=get_new_position(grid)
    assert(grid_get_value(grid,x,y)) == 0

def test_grid_add_new_tile():
    game_grid=create_grid(4)
    game_grid=grid_add_new_tile(game_grid)
    tiles = get_all_tiles(game_grid)
    assert 2 or 4 in tiles


def test_long_value_with_theme():
    grid =[[2048, 16, 32, 0], [0, 4, 0, 2], [0, 0, 0, 32], [512, 1024, 0, 2]]
    assert long_value_with_theme(grid,"0") == 4
    assert long_value_with_theme(grid,"1") == 2
    assert long_value_with_theme(grid,"2") == 1
    grid = [[16, 4, 8, 2], [2, 4, 2, 128], [4, 512, 32, 4096], [1024, 2048, 512, 2]]
    assert long_value_with_theme(grid,"0") == 4
    assert long_value_with_theme(grid,"1") == 2
    assert long_value_with_theme(grid,"2") == 1


def test_move_row_left():

    assert move_row_left([0, 0, 0, 2]) == [2, 0, 0, 0]
    assert move_row_left([0, 2, 0, 4]) == [2, 4, 0, 0]
    assert move_row_left([2, 2, 0, 4]) == [4, 4, 0, 0]
    assert move_row_left([2, 2, 2, 2]) == [4, 4, 0, 0]
    assert move_row_left([4, 2, 0, 2]) == [4, 4, 0, 0]
    assert move_row_left([2, 0, 0, 2]) == [4, 0, 0, 0]
    assert move_row_left([2, 4, 2, 2]) == [2, 4, 4, 0]
    assert move_row_left([2, 4, 4, 0]) == [2, 8, 0, 0]
    assert move_row_left([4, 8, 16, 32]) == [4, 8, 16, 32]

def test_move_row_right():

    assert move_row_right([2, 0, 0, 0]) == [0, 0, 0, 2]
    assert move_row_right([0, 2, 0, 4]) == [0, 0, 2, 4]
    assert move_row_right([2, 2, 0, 4]) == [0, 0, 4, 4]
    assert move_row_right([2, 2, 2, 2]) == [0, 0, 4, 4]
    assert move_row_right([4, 2, 0, 2]) == [0, 0, 4, 4]
    assert move_row_right([2, 0, 0, 2]) == [0, 0, 0, 4]
    assert move_row_right([2, 4, 2, 2]) == [0, 2, 4, 4]
    assert move_row_right([2, 4, 4, 0]) == [0, 0, 2, 8]
    assert move_row_right([4, 8, 16, 32]) == [4, 8, 16, 32]

def test_move_grid():
    assert move_grid([[2,0,0,2], [4, 4, 0, 0], [8, 0, 8, 0], [0, 2, 2, 0]],"g") == [[4,0,0,0], [8, 0, 0, 0], [16, 0, 0, 0], [4, 0, 0, 0]]
    assert move_grid([[2,0,0,2], [4, 4, 0, 0], [8, 0, 8, 0], [0, 2, 2, 0]],"d") == [[0,0,0,4], [0, 0, 0, 8], [0, 0, 0, 16], [0, 0, 0, 4]]
    assert move_grid([[2,0,0,2], [2, 4, 0, 0], [8, 4, 2, 0], [8, 2, 2, 0]],"h") == [[4,8,4,2], [16, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    assert move_grid([[2,0,0,2], [2, 4, 0, 0], [8, 4, 2, 0], [8, 2, 2, 0]],"b") == [[0, 0, 0, 0], [0, 0, 0, 0],[4,8,0,0],[16, 2, 4, 2]]

def test_is_full():
    assert is_full([[2,4],[8,64]]) == True
    assert is_full([[2,4],[8,0]]) == False







