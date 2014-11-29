from src.infrastructure.connectors import PostGreConnector
from src.poi.sound import SoundPoi


if __name__ == "__main__":
    pgconn = PostGreConnector(dbname='daydream', host='localhost', user='daydream', password='daydream')
    pgconn.connect()
    q = """
        SELECT
            sound_poi_id,
            sound_poi,
            location,
            content
        FROM sound_pois"""

    records = pgconn.query(q)
    sounds = [SoundPoi(record[0], record[1], record[2], record[3]) for record in records]
    for sound in sounds:
        sound.render()
