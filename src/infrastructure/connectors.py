import psycopg2


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
            self.conn = psycopg2.connect(dbname=self.dbname,
                                         host=self.host,
                                         user=self.user,
                                         password=self.password)
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
