from player import *

class Game():
    players = []
    endgame = False

    def add_player(self, name):
        new_player = Player(name)
        self.players.append(new_player)

    def remove_player(self, player_to_remove_index):
        del self.players[int(player_to_remove_index)-1]

    def get_players(self):
        print ('\n************************')
        print ('##  Player Name   Score')
        print('************************')
        for index, player in enumerate(self.players):
            print(str(index+1),' ', player)

        print()
        return self.players

    def get_action(self):
        options = { 'player_roll_dice': 'a) Current player rolls di',
                    'player_ends_turn': 'b) Current Player stops rolling',
                    'add_player':       'c) Add player',
                    'remove_player':    'd) Remove Player',
                    'quit_game':        'e) Quit game.'}

        self.get_players()

        for k, v in options.items():
            print (v)

        selection = input('Select option: ')

        if selection == 'a':
            pass
        elif selection == 'b':
            pass
        elif selection == 'c':
           new_player_name = input("Enter New Player's name: ")
           self.add_player(new_player_name)
        elif selection == 'd':
            player_to_remove = input("Which player should be removed (number)? ")
            self.remove_player(player_to_remove)
        elif selection == 'e':
            self.endgame = True
        if self.endgame != True:
            self.get_action()

    def __init__(self):
        pass

if __name__ == '__main__':
    mygame = Game()
    mygame.get_action()