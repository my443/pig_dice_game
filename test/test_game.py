import pytest
from src.game import *

def test_players_when_new_game_starts():
    new_game = Game()

    assert len(new_game.get_players()) == 0

def test_add_players():
    new_game = Game()
    new_game.add_player('John')
    new_game.add_player('Amy')

    assert len(new_game.get_players()) == 2


def test_add_players():
    new_game = Game()
    new_game.add_player('John')
    new_game.add_player('Amy')
    player_list = [str(x) for x in new_game.get_players()]

    assert player_list == ['John      ', 'Amy       ']
