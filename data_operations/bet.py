from dataclasses import dataclass


@dataclass
class Bet:
    player_name : str
    driver: str = ""
    bet_type: str = ""
    wins: int = 0
    losses: int  = 0
    finish:  int = 0
    win_percentage: float = 0
    losses_percentage: float = 0
