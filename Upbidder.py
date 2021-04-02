from typing import List, Dict
import API

class upbidder(API.PlayerType):

    def action(
        myDie: List[int],
        otherDie: Dict[str, int],
        previousBids: List[Dict[str, typing.Any]]
      ):
        if (len(previousBids) == 0):
          return Bid(6, 1)
        previousBid = previousBids[-1]["bid"]
        print("Raising bid " + str(previousBid))
        return API.Bid(previousBid.die, previousBid.count + 1)




