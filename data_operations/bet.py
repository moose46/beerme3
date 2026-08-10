from dataclasses import dataclass


@dataclass
class Bet:
    player_name: str
    wins: int
    driver: str
    finish: int
