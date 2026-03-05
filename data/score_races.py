from collections import defaultdict
from pathlib import Path
import psycopg
from psycopg.rows import dict_row
import db_connection
import db_connection as postgres_db

class ScoreTheRaces:
    def __init__(self):
        self.connection = psycopg.connect(
            dbname="beerme3",
            user="bob",
            password="admin",
            host="localhost",  # or your database server's IP
            port="5432"  # default PostgreSQL port
            , row_factory=dict_row
        )
        print("Connection successful!")
        self.cursor = self.connection.cursor()
    def get_results(self):
        return self.cursor.execute("""
                            select
	                            track,
	                            driver,
	                            pos,
                                case
                                    when greg_pick = true then 'GREG'
                                    when bob_pick = true then 'BOB'
                                end as pick
                            from
                                    nascar_results nr
                            where
                                    nr.greg_pick is not false
                                or bob_pick is not false
""").fetchall()

if __name__ == "__main__":
    scoreTheRaces = ScoreTheRaces()
    results = scoreTheRaces.get_results()
    for row in results:
        print(row)