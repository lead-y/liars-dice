import Engine


import Upbidder
import LieCaller

## The order of these tests is convenient - they build upon previous test runs,
# so it's a lot easier to debug them in the order they run.

def rollTest():
    rollResults = Engine.reroll({"player1": 3, "player2": 4})
    assert len(rollResults["player1"]) == 3, "Expected 3 die for player 1, got " + str(rollResults)
    assert len(rollResults["player2"]) == 4, "Expected 4 die for player 2, got " + str(rollResults)
    print("RollTest passed!")

rollTest()

def countOfTest():
    threes = Engine.countOf(3, {"player1": [1,2], "player2": [3,4]})
    assert threes == 1, "Expected to count one 3"
    fours = Engine.countOf(4, {"player1": [1,2,4], "player2": [3,4,3,4]})
    assert fours == 3, "Expected to count three 4s"
    fives = Engine.countOf(5, {"player1": [1,2,4], "player2": [3,4,3,4]})
    assert fives == 0, "Expected to count zero 5s"
    sixes = Engine.countOf(6, {"player1": [6], "player2": [2,3]})
    assert sixes == 1, "Expected to count zero 5s"
    print("CountOfTest Passed!")

countOfTest()

def roundTest():
    player1 = Upbidder.upbidder()
    player2 = LieCaller.LieCaller()
    players = [player1, player2]
    diceState = {player1: [5], player2: [2,3]}
    loosers = Engine.round(diceState, players)
    assert loosers[0] == 0, "Expected upbidder to bid 6,1 and liecaller to call it, winning. Instead got loosers " + str(loosers)
    diceState = {player1: [6], player2: [2,3]}
    loosers = Engine.round(diceState, players)
    assert loosers[0] == 1, "Expected upbidder to bid 6,1 and liecaller to call it, losing. Instead got loosers " + str(loosers)

roundTest()

def engineTest():
    Engine.game([Upbidder.upbidder(), LieCaller.LieCaller()])

engineTest()

