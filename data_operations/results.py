import dataclasses

HEADER = "POS	DRIVER	CAR	MANUFACTURER	LAPS	START	LED	PTS	BONUS   PENALTY"
from results_csv import *
@dataclasses.dataclass
class RaceResults:

    results_id: int
    race_id: int
    track_id: int
    manufacturer_name: str
    driver_id: int
    pos: str
    driver: str
    car: str
    manufacturer: str
    laps: str
    start: str
    led: str
    penalty: str


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
