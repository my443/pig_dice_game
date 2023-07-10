# Pig (Dice Game)

This is an implementation of the Pig Dice Game. Rules for this game can be [found here](https://en.wikipedia.org/wiki/Pig_(dice_game))

## Development Notes (structure)

* The game is the entry-point object
* A game has players.
  * Attributes:
    * Score
    * Nome
* A player can take a turn.
  * Attributes:
    * Turn_Status (Active or Ended)
      * Active: When you are still able to role
      * Ended: When you role a 1 our you quit your turn. 
    * Turn_Score - The score for the current turn. Becomes 0 if you role a 1.


## Possibilities
This implementation is intended to later be extensible so that it can accomodate possible: 
- Machine learning - by logging each person's turns we the machine can learn the optimal way to win the game. 
- REST framework implementation - for user interaction (GUI)
