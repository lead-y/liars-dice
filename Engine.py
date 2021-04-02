import API

import Upbidder
import LieCaller

from typing import Dict, List

from random import randInt

playerTypes = [Upbidder.upbidder, LieCaller.LieCaller]

## Play a game, which consists of multiple rounds until 
## only one player has die left.
def game(numPlayers):
    players = [playerTypes[i]() for i in [0,1]]
    diceCounts = {player: 5 for player in players}
    diceState = reroll(diceCounts)
    round(diceState)


## Reroll the specified number of die for all players.
def reroll(diceCounts: Dict[PlayerType, int]) -> Dict[PlayerType, List[int]]:
    return {player: [randint(1, 6) for i in range(numDie)] for (player, numdie) in enumerate(diceCounts)}

## Complete a round by giving players dice, and letting
## players take turns taking actions until someone 
## makes an illegal bid, calls "liar", or calls "spot on".
def round(diceState: Dict[str, List[int]], players: List[PlayerType]):
    currentPlayer = 0
    previousBids = []

    while (len(previousBids) < 1000): # Next player takes their turn
        action = players[currentPlayer].action(
            myDie = diceState[players[currentPlayer]],
            otherDie = {player: len(die) for (player, die) in  diceState},
            previousBids = previousBids
        )

        if (action == "liar"):
            # check who's wrong
            # return the player(s) who lose a die.
            raise "Not implemented yet"

        if (action == "spot on"):
            raise "Not implemented yet"

        ## TODO check if is a bid, then if is a valid bid

        else: 
            previousBids.append({
                "player": str(currentPlayer), 
                "bid": action
                })

