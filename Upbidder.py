from typing import List, Dict, Any
import API

class upbidder(API.PlayerType):

    def action(
        self,
        myDie: List[int],
        otherDie: Dict[str, int],
        previousBids: List[Dict[str, Any]]
      ):
        if (len(previousBids) == 0):
          return API.Bid(6, 1)
        previousBid = previousBids[-1]["bid"]
        print("Raising bid " + str(previousBid))
        return API.Bid(previousBid.die, previousBid.count + 1)




