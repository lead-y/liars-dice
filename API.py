"""
How do I make a player?

The API is to override the PlayerType class and override the function
`action` that takes in information about the game state and outputs an action.

Actions can be either "liar", "spot on", or any valid bid.


If you need to store state between rounds, that should be stored in instance variables.

The engine must import your class & will run it against other class instances in a tournament.

If your action isn't valid, you lose that round as if you had made a high bid & been called liar.





A minimal player that always bids up:

class myPlayer:
  def action(
    self,
    myDie: List[int],
    dieCounts: Dict[playerName: str, int],
    previousBids: List[{"player": str, "bid": Bid}]
    ):
    lastBid = previousBids[-1]["bid"]
    return Bid(lastBid.die, lastBid.count + 1)


"""

from typing import Dict, List, Any

class Bid:
    def __init__(self, die, count):
        self.die = die
        self.count = count
    def __str__(self):
        return str({"die": self.die, "count": self.count})

class PlayerType:
    def __init__(self):
        print ("Initializing player without any state.")
    
    def action(
        self,
        myDie: List[int],
        otherDie: Dict[str, int],
        previousBids: List[Dict[str, Any]]
    ):
        raise Exception("""Your player must implement the `action` function. Action should take in the current game state and output either a Bid, the string "liar", or the string "spot on" """)

    
    












