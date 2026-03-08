import psycopg
from psycopg.rows import dict_row


class ScoreTheRaces:
    def __init__(self):
        self.connection = psycopg.connect(
            dbname="beerme3",
            user="bob",
            password="admin",
            host="localhost",  # or your database server's IP
            port="5432",  # default PostgreSQL port
            row_factory=dict_row,
        )
        print("Connection successful!")
        self.cursor = self.connection.cursor()

    def get_results(self):
        return self.cursor.execute("""
                                   select track,
                                          driver,
                                          pos,
                                          case
                                              when greg_pick = true then 'GREG'
                                              when bob_pick = true then 'BOB'
                                              end as pick
                                   from nascar_results nr
                                   where nr.greg_pick is not false
                                      or bob_pick is not false
                                   """).fetchall()

    def get_results2(self):
        return self.cursor.execute("""
                                   select race_date,
                                          track,
                                          (select (pos,
                                                   driver)
                                           from nascar_results g
                                           where greg_pick = true
                                             and g.race_date = a.race_date
                                           group by pos,
                                                    driver)                 as greg,
                                          (select (pos,
                                                   driver)
                                           from nascar_results b
                                           where bob_pick = true
                                             and b.race_date = a.race_date) as bob
                                   from public.nascar_results a
                                   group by race_date,
                                            track""").fetchall()

    def get_results3(self):
        return self.cursor.execute("""
                                   select to_char(race_date, 'MM/DD/YYYY')  as race_date,
                                          track,
                                          (select (pos)
                                           from nascar_results g
                                           where greg_pick = true
                                             and g.race_date = a.race_date) as greg_pos,
                                          (select (driver)
                                           from nascar_results g
                                           where greg_pick = true
                                             and g.race_date = a.race_date) as greg_driver,
                                          (select (pos)
                                           from nascar_results b
                                           where bob_pick = true
                                             and b.race_date = a.race_date) as bob_pos,
                                          (select (driver)
                                           from nascar_results g
                                           where bob_pick = true
                                             and g.race_date = a.race_date) as bob_driver
                                   from public.nascar_results a
                                   group by race_date,
                                            track
                                   order by race_date desc;
                                   """).fetchall()


if __name__ == "__main__":
    scoreTheRaces = ScoreTheRaces()
    # results = scoreTheRaces.get_results()
    # results2 = scoreTheRaces.get_results2()
    results3 = scoreTheRaces.get_results3()
    # for row in results:
    #     print(row)
    # for row in results2:
    #     print(row)
    total_bob_beers = 0
    total_greg_beers = 0
    for row in results3:
        if row["greg_pos"] > row["bob_pos"]:
            row["greg_beer"] = 0
            if row["bob_pos"] == 1:
                row["bob_beer"] = 2
            else:
                row["bob_beer"] = 1
        if row["greg_pos"] < row["bob_pos"]:
            row["bob_beer"] = 0
            if row["greg_pos"] == 1:
                row["greg_beer"] = 2
            else:
                row["greg_beer"] = 1
        total_bob_beers += row["bob_beer"]
        total_greg_beers += row["greg_beer"]
        print(row)
    print(total_bob_beers)
    print(total_greg_beers)
