import API

from typing import Dict, List

from random import randint

## Play a game, which consists of multiple rounds until 
## only one player has die left.
def game(playerTypes: List[API.PlayerType]):
    print("Starting game")
    players = [playerTypes[i]() for i in [0,1]]
    diceCounts = {player: 5 for player in players}
    diceState = reroll(diceCounts)
    loosers = round(diceState, players)
    # Todo - decrement dice counts for the player who lost, check if the game is over, and start a new round.


## Reroll the specified number of die for all players.
def reroll(diceCounts: Dict[API.PlayerType, int]) -> Dict[API.PlayerType, List[int]]:
    return {
        player: [randint(1, 6) for i in range(diceCounts[player])] for player in diceCounts
        }

## Complete a round by giving players dice, and letting
## players take turns taking actions until someone 
## makes an illegal bid, calls "liar", or calls "spot on".
def round(diceState: Dict[API.PlayerType, List[int]], players: List[API.PlayerType]):
    currentPlayer = 0
    previousBids = []

    print("Starting round with dice state " + str(diceState))

    while (len(previousBids) < 1000): # Next player takes their turn
        print("Taking turn for player " + str(currentPlayer))
        
        action = players[currentPlayer].action(
            myDie = diceState[players[currentPlayer]],
            otherDie = {player: len(diceState[player]) for player in diceState},
            previousBids = previousBids
        )

        print("Player chose action " + str(action))

        if (action == "liar"):
            # check who's wrong
            # return the player(s) who lose a die.
            raise Exception("Not implemented yet")

        if (action == "spot on"):
            raise Exception("Not implemented yet")

        ## TODO check if is a bid, then if is a valid bid

        else: 
            previousBids.append({
                "player": str(currentPlayer), 
                "bid": action
                })

        # Advance to next player
        currentPlayer += 1
        if (currentPlayer > len(players)):
            currentPlayer = 0

