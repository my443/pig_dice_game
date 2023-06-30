import pytest
from src.player import *

def test_initial_player_score():
    new_player = Player('John')
    assert new_player.get_score() == 0

def test_score_after_it_is_set():
    new_player = Player('John')
    new_player.add_score(5)

    assert new_player.get_score() == 5

def test_that_player_has_uuid():
    new_player = Player('John')

    assert new_player.player_id is not None

def test_player_has_name():
    new_player = Player('John')

    assert new_player.name == 'John'