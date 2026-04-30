from collections import defaultdict


class BetData:
    def __getitem__(self, race_date):
        return self.individual_bets[race_date]

    def __init__(self) -> None:
        self.individual_bets = defaultdict()
        # self.individual_bets.setdefault("missing_key")
        self.individual_bets["02-15-2026"] = {
            "Greg": "William Byron",
            "Bob": "Ryan Blaney",
            "Track": "Daytona",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["02-22-2026"] = {
            "Greg": "Ryan Blaney",
            "Bob": "Chase Elliott",
            "Track": "Atlanta",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["03-01-2026"] = {
            "Greg": "Shane van Gisbergen",
            "Bob": "Tyler Reddick",
            "Track": "COTA",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["03-08-2026"] = {
            "Greg": "Ryan Blaney",
            "Bob": "Kyle Larson",
            "Track": "Phoenix",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["03-15-2026"] = {
            "Greg": "Kyle Larson",
            "Bob": "Christopher Bell",
            "Track": "Las Vegas",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["03-22-2026"] = {
            "Greg": "Denny Hamlin",
            "Bob": "Tyler Reddick",
            "Track": "Darlington",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["03-29-2026"] = {
            "Greg": "William Byron",
            "Bob": "Denny Hamlin",
            "Track": "Martinsville",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["04-12-2026"] = {
            "Greg": "Kyle Larson",
            "Bob": "Ty Gibbs",
            "Track": "Bristol",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["04-19-2026"] = {
            "Greg": "Kyle Larson",
            "Bob": "Tyler Reddick",
            "Track": "Kansas",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["04-26-2026"] = {
            "Greg"       : "Ryan Blaney",
            "Bob"        : "Tyler Reddick",
            "Track"      : "Talladega",
            "badge_color": "bg-warning text-dark",
        }

        # # start of can't pick a driver twice

    @property
    def get_bets(self):
        """_summary_

        Returns:
            Returns a list of dictionaries of all the current bet in date_information for Greg and Bob
            first pick starts at the first of the year and alternates each week
        """
        for first_pick, x in enumerate(self.individual_bets):
            self.individual_bets[x]["first_pick"] = "Greg" if first_pick % 2 else "Bob"
        return self.individual_bets
