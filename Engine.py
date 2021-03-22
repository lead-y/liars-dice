import API

import Upbidder

from typing import Dict, List

from random import randInt


print(
    Upbidder.upbidder().round(
        myDie = [1,1,1],
        otherDie = {"player2": 3, "player3": 5},
        previousBids = [API.Bid(2, 3), API.Bid(2, 4)]
    )
)

playerTypes = [Upbidder.upbidder]

def game(numPlayers):
    players = [playerTypes[i]() for i in [0,0]]
    diceCounts = {player: 5 for player in players}
    diceState = reroll(diceCounts)
    rount(diceState)



def reroll(diceCounts: Dict[PlayerType, int]) -> Dict[PlayerType, List[int]]:
    return {player: [randint(1, 6) for i in range(numDie)] for (player, numdie) in enumerate(diceCounts)}

def round(diceState: Dict[playerType, List[int]], players: List[PlayerType]):
    currentPlayer = 0
    action = players[currentPlayer].action(
        myDie = diceState[players[currentPlayer]],
        otherDie = 
    
    
    
    # TODO finish writing the first game and test it by running this file.
