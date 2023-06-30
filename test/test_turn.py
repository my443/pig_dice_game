import pytest
from src.turn import *


def test_class_setup_active_turn():
    new_turn = Turn()

    assert new_turn.get_turn_status() == new_turn.TurnStatus.Active


def test_adding_a_value():
    new_turn = Turn()

    new_turn.add_roll(5)
    new_turn.add_roll(6)

    assert new_turn.score_values == [5, 6]

def test_adding_values_ending_with_zero():
    new_turn = Turn()

    new_turn.add_roll(5)
    new_turn.add_roll(6)
    new_turn.add_roll(0)

    assert new_turn.score_values == [5, 6, 0]

def test_status_after_adding_zero():
    new_turn = Turn()

    new_turn.add_roll(5)
    new_turn.add_roll(6)
    new_turn.add_roll(0)

    assert new_turn.get_turn_status() == new_turn.TurnStatus.Ended

def test_get_total_score_when_last_roll_is_zero():
    new_turn = Turn()

    new_turn.add_roll(5)
    new_turn.add_roll(6)
    new_turn.add_roll(0)

    assert new_turn.get_score() == 0

def test_get_total_score():
    new_turn = Turn()

    new_turn.add_roll(5)
    new_turn.add_roll(6)

    assert new_turn.get_score() == 11

def test_end_turn():
    new_turn = Turn()
    new_turn.end_turn()

    assert new_turn.get_turn_status() == new_turn.TurnStatus.Ended
