import API

from typing import Dict, List

from random import randint, random

## This file holds the engine, which is responsible for actually
# playing players against each other in games (keeping game state & calling 
# 'action' on players appropriately.)
# 
# Each player instance gets a unique name, and other players can know that name.
# Within a game, players are put in an order and usually referenced by their position in this order. 
# Player order is not explicitly provided to players, but they can infer it from the previousBids list.

## Play a game, which consists of multiple rounds until 
## only one player has die left.
def game(playerInstances: List[API.PlayerType]):
    log("Starting game", 'gameEvent')
    players = [playerInstances[i] for i in [0,1]] # TODO shuffle
    diceCounts = {player: 5 for player in players}
    while (len(diceCounts) > 1):
        diceState = reroll(diceCounts)
        loosers = round(diceState, players)
        log("Loosers this round: "+ str(loosers), 'gameEvent')
        for index in loosers:
            player = players[index]
            diceCounts[player] -= 1
            if (diceCounts[player] == 0):
                log("Player " + str(index) + " is out of this game", 'gameEvent')
                del players[index]
                del diceCounts[player]
    log("Player " + str(players[0]) + " Wins!")

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

    log("Starting round with dice state " + str(diceState), 'debug')

    while (len(previousBids) < 1000): # Next player takes their turn
        log("Taking turn for player " + str(currentPlayer), 'gameEvent')
        
        action = players[currentPlayer].action(
            myDie = diceState[players[currentPlayer]],
            otherDie = {player: len(diceState[player]) for player in diceState},
            previousBids = previousBids
        )

        log("Player chose action " + str(action), 'gameEvent')

        if (action == "liar"):
            # check who's wrong
            # return the player(s) who lose a die.
            if (len(previousBids) == 0): ## If you call liar on the first turn, you lose.
                return [currentPlayer]
            previousBid: API.Bid = previousBids[-1]["bid"]
            previousPlayer = currentPlayer - 1 if currentPlayer > 0 else len(players) - 1
            totalCount = countOf(previousBid.die, diceState)
            log("Counted " + str(totalCount) + " for bid of " + str(previousBid))
            if (totalCount >= previousBid.count):
                return [currentPlayer]
            else:
                return [previousPlayer]

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
        if (currentPlayer > len(players) - 1):
            currentPlayer = 0

def countOf(dieToCount, diceState):
    return sum(
        [1 if die == dieToCount else 0 for player in diceState for die in diceState[player]]
    )

def log(message, level = 'debug'):
    print(message)

