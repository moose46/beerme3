from collections import defaultdict


class BetData2026_1:
    def __init__(self):
        self.individual_bets = defaultdict(dict)
        self.individual_bets["02-15-2026"] = {
            "Greg": {'Driver': "William Byron", "Finish": 0, "beers": 0},
            "Bob": {"Driver": "Ryan Blaney", "Finish": 0, "beers": 0},
            "Track": "Daytona",
            "badge_color": "bg-warning text-dark",
        }

        self.individual_bets["02-22-2026"] = {
            "Greg": {"Driver": "Ryan Blaney", "Finish": 0, "beers": 0},
            "Bob": {"Driver": "Chase Elliott", "Finish": 0, "beers": 0},
            "Track": "Atlanta",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["03-01-2026"] = {
            "Greg": {"Driver": "Shane van Gisbergen", "Finish": 0, "beers": 0},
            "Bob": {"Driver": "Tyler Reddick", "Finish": 0, "beers": 0},
            "Track": "COTA",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["03-08-2026"] = {
            "Greg": {"Driver": "Ryan Blaney", "Finish": 0, "beers": 0},
            "Bob": {"Driver": "Kyle Larson", "Finish": 0, "beers": 0},
            "Track": "Phoenix",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["03-15-2026"] = {
            "Greg": {"Driver": "Kyle Larson", "Finish": 0, "beers": 0},
            "Bob": {"Driver": "Christopher Bell", "Finish": 0, "beers": 0},
            "Track": "Phoenix",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["03-22-2026"] = {
            "Greg": {"Driver": "Denny Hamlin", "Finish": 0, "beers": 0},
            "Bob": {"Driver": "Tyler Reddick", "Finish": 0, "beers": 0},
            "Track": "Darlington",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["03-29-2026"] = {
            "Greg": {"Driver": "William Byron", "Finish": 0, "beers": 0},
            "Bob": {"Driver": "Denny Hamlin", "Finish": 0, "beers": 0},
            "Track": "Martinsville",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["04-12-2026"] = {
            "Greg": {"Driver": "Kyle Larson", "Finish": 0, "beers": 0},
            "Bob": {"Driver": "Ty Gibbs", "Finish": 0, "beers": 0},
            "Track": "Bristol",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["04-19-2026"] = {
            "Greg": {"Driver": "Kyle Larson", "Finish": 0, "beers": 0},
            "Bob": {"Driver": "Tyler Reddick", "Finish": 0, "beers": 0},
            "Track": "Kansas",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["04-26-2026"] = {
            "Greg": {"Driver": "Ryan Blaney", "Finish": 0, "beers": 0},
            "Bob": {"Driver": "Tyler Reddick", "Finish": 0, "beers": 0},
            "Track": "Talladega",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["05-03-2026"] = {
            "Greg": {"Driver": "Denny Hamlin", "Finish": 0, "beers": 0},
            "Bob": {"Driver": "Carson Hocevar", "Finish": 0, "beers": 0},
            "Track": "Texas",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["05-10-2026"] = {
            "Greg":{"Driver": "Shane van Gisbergen","Finish":0,"beers":0},
            "Bob": {"Driver":"Ty Gibbs","Finish":0,"beers":0},
            "Track": "Watkins Glen",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["05-24-2026"] = {
            "Greg": {"Driver":"Denny Hamlin","Finish":0,"beers":0},
            "Bob": {"Driver":"Ross Chastain","Finish":0,"beers":0},
            "Track": "Charlotte",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["05-31-2026"] = {
            "Greg": {"Driver":"Tyler Reddick","Finish":0,"beers":0},
            "Bob":{"Driver":"Denny Hamlin","Finish":0,"beers":0},
            "Track": "Nashville",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["06-07-2026"] = {
            "Greg":{"Driver": "Kyle Larson","Finish":0,"beers":0},
            "Bob": {"Driver":"Tyler Reddick","Finish":0,"beers":0},
            "Track": "Michigan",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["06-14-2026"] = {
            "Greg": {"Driver":"Denny Hamlin","Finish":0,"beers":0},
            "Bob": {"Driver":"Chase Briscoe","Finish":0,"beers":0},
            "Track": "Pocono",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["06-21-2026"] = {
            "Greg": {"Driver":"Connor Zilisch","Finish":0,"beers":0},
            "Bob": {"Driver":"Shane van Gisbergen","Finish":0,"beers":0},
            "Track": "Coronado",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["06-28-2026"] = {
            "Greg": {"Driver":"Shane van Gisbergen","Finish":0,"beers":0},
            "Bob": {"Driver":"Kyle Larson","Finish":0,"beers":0},
            "Track": "Sonoma Raceway",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["07-05-2026"] = {
            "Greg":{"Driver": "Kyle Larson","Finish":0,"beers":0},
            "Bob": {"Driver":"Denny Hamlin","Finish":0,"beers":0},
            "Track": "Chicagoland Speedway",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["07-12-2026"] = {
            "Greg":{"Driver": "Ryan Blaney","Finish":0,"beers":0},
            "Bob": {"Driver":"Chase Elliott","Finish":0,"beers":0},
            "Track": "EchoPark Speedway",
            "badge_color": "bg-warning text-dark",
        }

    def __getitem__(self, race_date):  # '02-15-2026'
        return self.individual_bets[race_date]


class BetData2026:
    def __getitem__(self, race_date):  # '02-15-2026'
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
            "Greg": "Ryan Blaney",
            "Bob": "Tyler Reddick",
            "Track": "Talladega",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["05-03-2026"] = {
            "Greg": "Denny Hamlin",
            "Bob": "Carson Hocevar",
            "Track": "Texas",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["05-10-2026"] = {
            "Greg": "Shane van Gisbergen",
            "Bob": "Ty Gibbs",
            "Track": "Watkins Gleen",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["05-24-2026"] = {
            "Greg": "Denny Hamlin",
            "Bob": "Ross Chastain",
            "Track": "Charlotte",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["05-31-2026"] = {
            "Greg": "Tyler Reddick",
            "Bob": "Denny Hamlin",
            "Track": "Nashville",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["06-07-2026"] = {
            "Greg": "Kyle Larson",
            "Bob": "Tyler Reddick",
            "Track": "Michigan",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["06-14-2026"] = {
            "Greg": "Denny Hamlin",
            "Bob": "Chase Briscoe",
            "Track": "Pocono",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["06-21-2026"] = {
            "Greg": "Connor Zilisch",
            "Bob": "Shane van Gisbergen",
            "Track": "Coronado",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["06-28-2026"] = {
            "Greg": "Shane van Gisbergen",
            "Bob": "Kyle Larson",
            "Track": "Sonoma Raceway",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["07-05-2026"] = {
            "Greg": "Kyle Larson",
            "Bob": "Denny Hamlin",
            "Track": "Chicagoland Speedway",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["07-12-2026"] = {
            "Greg": "Ryan Blaney",
            "Bob": "Chase Elliott",
            "Track": "EchoPark Speedway",
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
        # for first_pick, x in enumerate(self.individual_bets):
        #     self.individual_bets[x]["first_pick"] = "Greg" if first_pick % 2 else "Bob"
        return self.individual_bets


if __name__ == "__main__":
    """_summary_
    Returns: List of races
    """
    bets = BetData2026()
    results = bets.get_bets
    for result in results:
        print(f"{results[result]}")
