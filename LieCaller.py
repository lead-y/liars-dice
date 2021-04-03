from typing import List, Dict, Any
import API

class LieCaller(API.PlayerType):

    def action(
        self,
        myDie: List[int],
        otherDie: Dict[str, int],
        previousBids: List[Dict[str, Any]]
      ):
        return "liar"




