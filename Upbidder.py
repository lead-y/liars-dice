from typing import List, Dict
import API

class upbidder(API.PlayerType):

    def action(
        myDie: List[int],
        otherDie: Dict[str, int],
        playerOrder: List[str],
        previousBids: List[API.Bid]
      ):
        if (len(previousBids) == 0):
          return Bid(6, 1)
        previousBid = previousBids[-1]
        print("Raising bid " + str(previousBid))
        return API.Bid(previousBid.die, previousBid.count + 1)




