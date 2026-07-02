import db_connection as db
import json

tracks_found = 0
db = db.PostgreSQL()
cursor = db.get_cursor()
with open('data\\2026_races.json', "r") as file:
    races = json.load(file)
    for row in races:
        print(row)
        """
        Check to see if track exists in the track table
        if it does not exist , create it and return the track id
        else return the track id
        :param track:
        """
        try:
            sql = """
                  insert into tracks (track_name, id)
                  select %s, nextval('seq_track_id')
                  where not exists  (select track_name
                                     from tracks
                                     where track_name = %s)
                  """
            cursor.execute(sql, (row['track'],row['track']))
            db.connection.commit()
            tracks_found += 1
        except Exception as e:
            db.connection.rollback()
            exit(e.__str__())
# cursor.execute(f"select * from tracks order by track_name")
# for row in cursor.fetchall():
