from enum import *
import random

class Turn():
    current_score = 0
    score_values = []
    TurnStatus = Enum('TurnStatus', ['Active', 'Ended'])
    curren_status = TurnStatus.Active

    def add_roll(self):
        roll = random.randint(1, 6)

        if roll == 1:
            self.end_turn('rolled a 1')

        if self.get_turn_status() == self.TurnStatus.Active:
            self.score_values.append(roll)

        return roll


    def get_score(self):
        if self.get_turn_status() == self.TurnStatus.Active:
            self.current_score = sum(self.score_values)
            return self.current_score
        else:
            self.current_score = 0
            return self.current_score

    def get_turn_status(self):
        return self.curren_status

    def turn_is_active(self):
        return self.get_turn_status() != self.TurnStatus.Ended

    def end_turn(self, reason):
        if reason != 'player':
            self.score_values = []

        self.curren_status = self.TurnStatus.Ended

        return  self.TurnStatus

    def __init__(self):
        self.current_status = self.TurnStatus.Active
        self.score_values = []

    def __str__(self):
        return f'***************************************' \
               f'\nCurrent score: {self.get_score()}' +\
                f'\n{self.get_turn_status()}\n' \
                f'***************************************\n'

if __name__ == '__main__':
    pass
