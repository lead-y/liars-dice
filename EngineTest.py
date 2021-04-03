import Engine


import Upbidder
import LieCaller

def rollTest():
    rollResults = Engine.reroll({"player1": 3, "player2": 4})
    assert len(rollResults["player1"]) == 3, "Expected 3 die for player 1 but got " + str(rollResults)
    assert len(rollResults["player2"]) == 4, "Expected 4 die for player 2 but got " + str(rollResults)

rollTest()

def engineTest():
    Engine.game([Upbidder.upbidder, LieCaller.LieCaller])

engineTest()

