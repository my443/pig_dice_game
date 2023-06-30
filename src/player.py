class Player():
    player_id = ''
    name = ''
    score = 0

    def add_score(self, score):
        self.score = self.score + score

    def get_score(self):
        return self.score

    def __init__(self, name, id):
        self.player_id = id
        self.name = name
