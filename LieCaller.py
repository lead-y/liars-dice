from typing import List, Dict
import API

class LieCaller(API.PlayerType):

    def action(
        myDie: List[int],
        otherDie: Dict[str, int],
        playerOrder: List[str],
        previousBids: List[API.Bid]
      ):
        return "liar"




