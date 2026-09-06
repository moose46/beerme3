import dataclasses
import sqlite3
from dataclasses import astuple, asdict


@dataclasses.dataclass
class RaceResults:
    # results_id: int
    race_id: int
    track_id: int
    manufacturer: str = dataclasses.field()
    driver_id: int
    pos: str
    driver_name: str
    car: int
    laps: int
    start: int
    led: int
    pts: int
    bonus: int
    penalty: int
    espn_driver_url: str


class RaceResultsDB:
    def __init__(self, db_path="bets.db"):
        self.db_path = db_path

    def insert_results(self, race: RaceResults):
        race_dict = asdict(race)
        race_tuple = tuple(race_dict.values())
        race_fields = tuple(race_dict.keys())
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(f"insert into results {race_fields} values (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                               astuple(race), )
                conn.commit()
        except sqlite3.IntegrityError as err:
            print(f"insert_results() Problem with {race.race_id} {race.driver_name} {err} ")

    def csv_create_file(self):
        year = self._race_date[6:10]
        month = self._race_date[:2]
        day = self._race_date[3:5]
        output_file_name = f"{TARGET_RESULTS}/{month}-{day}-{year}.csv"
        csv_data = []
        csv_file = open(output_file_name, "w")
        # write the header names
        csv_file.write(",".join(self.csv_headers))

        # for result in self.race_results_dict:
        #     print(result)
        csv_file.write("\n")
        for race in self.race_results_dict:
            data_list = []
            for header_name in self.csv_headers:
                data_list.append(race[header_name])
            csv_file.write(",".join(data_list))
            csv_file.write("\n")
        csv_file.close()
        pass
