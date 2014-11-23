import psycopg2
from src.poi.sound import SoundPoi

class PostGreConnector:
    """Handles queries to PostGreSQL database."""
    def __init__(self, dbname, host, user, password):
        self.dbname = dbname
        self.user = user
        self.host = host
        self.password = password
        self.conn = None

    def connect(self):
        """Connect to PostGreSQL database."""
        try:
            self.conn = psycopg2.connect(dbname='daydream', host='localhost', user='daydream', password='daydream')
        except:
            print("I am unable to connect to the database")

    def query(self, query):
        """Execute a query against the database.

        :param query: The query to run
        :return: List of returned tuples
        """
        cur = self.conn.cursor()
        cur.execute(query)
        return cur.fetchall()

    def output(self,records):
        """Output records (for test purposes).

        :param records: List of tuples to print out
        """
        for record in records:
            print(record[0], record[1])

if __name__ == "__main__":
    pgconn = PostGreConnector(dbname='daydream', host='localhost', user='daydream', password='daydream')
    pgconn.connect()

    records = pgconn.query('SELECT location, content FROM sound_pois')
    sounds = [SoundPoi(record[0], record[1]) for record in records]
    for sound in sounds:
        sound.render()
