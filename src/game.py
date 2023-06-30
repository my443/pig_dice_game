from src.player import *

class Game():
    players = []

    def add_player(self, name):
        new_player = Player(name)
        self.players.append(new_player)

    def remove_player(self):
        pass

    def get_players(self):
        return self.players

    def __init__(self):
        pass