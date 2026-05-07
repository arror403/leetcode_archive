import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:

    return [len(players), players.size//len(players)]