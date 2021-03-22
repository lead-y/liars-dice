from typing import List, Dict
import API

class upbidder(API.PlayerType):

    def action(
        myDie: List[int],
        otherDie: Dict[str, int],
        playerOrder: List[str],
        previousBids: List[API.Bid]
      ):
        previousBid = previousBids[-1]
        print("Raising bid " + str(previousBid))
        return API.Bid(previousBid.die, previousBid.count + 1)




