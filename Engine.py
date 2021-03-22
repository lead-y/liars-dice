import API

import Upbidder
import LieCaller

from typing import Dict, List

from random import randInt


print(
    Upbidder.upbidder().round(
        myDie = [1,1,1],
        otherDie = {"player2": 3, "player3": 5},
        previousBids = [API.Bid(2, 3), API.Bid(2, 4)]
    )
)

playerTypes = [Upbidder.upbidder, LieCaller.LieCaller]

def game(numPlayers):
    players = [playerTypes[i]() for i in [0,1]]
    diceCounts = {player: 5 for player in players}
    diceState = reroll(diceCounts)
    rount(diceState)



def reroll(diceCounts: Dict[PlayerType, int]) -> Dict[PlayerType, List[int]]:
    return {player: [randint(1, 6) for i in range(numDie)] for (player, numdie) in enumerate(diceCounts)}

def round(diceState: Dict[playerType, List[int]], players: List[PlayerType]):
    currentPlayer = 0
    previousBids = []

    action = players[currentPlayer].action(
        myDie = diceState[players[currentPlayer]],
        otherDie = {player: len(die) for (player, die) in  diceState},
        playerOrder = players,
        previousBids = previousBids
    )

    if (action == "liar"):
        # check who's wrong
        # return the player(s) who lose a die.
        raise "Not implemented yet"

    else: ## TODO check if is a bid, then if is a valid bid
        previousBids.append(action)
        return {"previousBids": previousBids}

