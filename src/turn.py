from enum import *

class Turn():
    current_score = 0
    score_values = []
    TurnStatus = Enum('TurnStatus', ['Active', 'Ended'])
    curren_status = TurnStatus.Active
    chose_to_end_turn = 0

    def add_roll(self, roll):
        if self.get_turn_status() == self.TurnStatus.Active:
            self.score_values.append(roll)

    def get_score(self):
        if self.get_turn_status() == self.TurnStatus.Active:
            return sum(self.score_values)
        else:
            return 0

    def get_turn_status(self):
        if len(self.score_values) > 0 and self.score_values[-1] == 0 or self.chose_to_end_turn == 1:
            return self.TurnStatus.Ended
        else:
            return self.TurnStatus.Active

    def end_turn(self):
        self.chose_to_end_turn = 1

    def __init__(self):
        self.current_status = self.TurnStatus.Active
        self.score_values = []
        pass

if __name__ == '__main__':
    new_turn = Turn()

    new_turn.add_roll(5)
    new_turn.add_roll(6)
    new_turn.add_roll(0)
    print (new_turn.score_values)
    print (new_turn.score_values[-1])
    print(new_turn.get_turn_status())
