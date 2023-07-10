from player import *
from turn import *
import os

class Game():
    players = []
    endgame = False
    current_turn_player = None
    current_turn_details = Turn()

    def add_player(self, name):
        new_player = Player(name)
        self.players.append(new_player)

        # If you have just one person when you add a player,
        # That is where the game starts
        if len(self.players) == 1:
            self.assign_current_turn()
            self.new_turn()

    def remove_player(self, player_to_remove_index):
        del self.players[int(player_to_remove_index)-1]
        ## TODO - when you remove a player, the current turn might need to be changed.

    def get_players(self):
        print ('\n************************')
        print ('##  Player Name   Score')
        print('************************')
        for index, player in enumerate(self.players):
            print(str(index+1),' ', player)

        print()
        return self.players

    def assign_current_turn(self):
        self.current_turn_player = 0

    def get_turn(self):
        turn = self.current_turn_details
        if len(self.players) > 0:
            print(f'Current Player: {self.players[self.current_turn_player].name}\n')
        print (turn)

        return turn

    def new_turn(self):
        new_turn = Turn()

        if self.current_turn_player + 1 > len(self.players):
            self.current_turn_player = 0
        else:
            self.current_turn_player + 1

        self.current_turn_details = new_turn

    def roll_dice(self):
        myturn = self.current_turn_details
        roll = myturn.add_roll()
        return roll

    def get_action(self):
        options = { 'player_roll_dice': 'a) Current player rolls dice',
                    'player_ends_turn': 'b) Current Player stops rolling',
                    'add_player':       'c) Add player',
                    'remove_player':    'd) Remove Player',
                    'quit_game':        'e) Quit game.'}

        os.system('cls')

        self.get_players()
        this_turn = self.get_turn()
        print (this_turn)
        # if len(self.players) > 1:
        #     if this_turn.turn_is_active() == False:
        #         self.new_turn()


        for k, v in options.items():
            print (v)

        selection = input('Select option: ')

        if selection == 'a':
            roll = self.roll_dice()
            print('roll: ', roll)
            print (self.current_turn_details.get_score())
            input('')
        elif selection == 'b':
            for i in range(10): print('ending turn now')
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