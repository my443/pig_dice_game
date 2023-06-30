from enum import *

class Turn():
    current_score = 0
    score_values = []
    TurnStatus = Enum('TurnStatus', ['Active', 'Ended'])
    curren_status = TurnStatus.Active
    chose_to_end_turn = False

    def add_roll(self, roll):
        if self.get_turn_status() == self.TurnStatus.Active:
            self.score_values.append(roll)

    def get_score(self):
        if self.get_turn_status() == self.TurnStatus.Active:
            return sum(self.score_values)
        else:
            return 0

    def set_turn_status(self):
        if len(self.score_values) > 0 and self.score_values[-1] == 0 or self.chose_to_end_turn == True:
            self.curren_status = self.TurnStatus.Ended
        else:
            self.curren_status = self.TurnStatus.Active

    def get_turn_status(self):
        self.set_turn_status()
        return self.curren_status

    def end_turn(self):
        self.chose_to_end_turn = True

    def __init__(self):
        self.current_status = self.TurnStatus.Active
        self.score_values = []
        pass

if __name__ == '__main__':
    pass
