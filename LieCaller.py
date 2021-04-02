from typing import List, Dict
import API

class LieCaller(API.PlayerType):

    def action(
        myDie: List[int],
        otherDie: Dict[str, int],
        previousBids: List[Dict[str, typing.Any]]
      ):
        return "liar"




