import shutil
import sys
from pathlib import Path

TARGET_BEERME_BET_DATA2026 = r"C:\Users\me\Documents\VisualCodeSource\beerme2\data"
# SOURCE_BEERME_BET_DATA2026 = r"C:\Users\me\PycharmProjects\BeerMe3\betData2026.py"


def copy_race_results_csv(prace_dates: list):
    for race in prace_dates:
        # print(f"{TARGET_RESULTS_BEER_ME}\\{race}")
        my_file = Path().parent.absolute().joinpath(f"..\\data\\{race}")
        if  my_file.is_file():
            print(
                f"-- Copying {Path(my_file)} to "
                f"{TARGET_BEERME_BET_DATA2026}")
            shutil.copy2(my_file, f"{TARGET_BEERME_BET_DATA2026}")  # copy2 preserves
        else:
            print(
                f"-- File Not Found {Path(my_file)} to \n "
            )


if __name__ == "__main__":
    try:
        race_results_csv_filename = sys.argv[1]
    except IndexError as e:
        race_results_csv_filename = '02-04-2026.csv'

    copy_race_results_csv(prace_dates=[race_results_csv_filename])
