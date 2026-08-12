import dataclasses

COLUMNS = "POS	DRIVER	CAR	MANUFACTURER	LAPS	START	LED	PTS	BONUS	PENALTY"
TARGET_RESULTS = f"./data"
@dataclasses.dataclass
class CSVResults:
    pos: int
    driver: str
    car: int
    manufacturer: str
    laps: int
    start: int
    led: int
    pts: int
    bonus: int
    penalty: int
