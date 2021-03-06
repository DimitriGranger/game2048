from game2048.grid_2048 import *
from game2048.textual_2048 import *
import pytest


def test_read_player_command(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x : 'd')
    x = read_player_command()
    assert x == 'd'


def test_read_size_grid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x : 3)
    x = read_size_grid()
    assert x == 3


def test_read_theme_grid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x : '2')
    x = read_theme_grid()
    assert x == '2'


