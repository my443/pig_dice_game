import uuid

class Player():
    player_id = ''
    name = ''
    score = 0

    def add_score(self, score_to_add):
        self.score = self.score + score_to_add

    def get_score(self):
        return self.score

    def __init__(self, name):
        self.player_id = uuid.uuid4()
        self.name = name
        self.score = 0

    def __str__(self):
        return  f"{self.name.ljust(10, ' ')}      {self.score}"