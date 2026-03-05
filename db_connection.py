import psycopg


class PostgreSQL:
    def __init__(self):
        self.cursor = None
        pass

    def get_cursor(self):
        # Connect to PostgreSQL
        connection = psycopg.connect(
            dbname="beerme3",
            user="bob",
            password="admin",
            host="localhost",  # or your database server's IP
            port="5432"  # default PostgreSQL port
        )

        self.cursor = connection.cursor()
        print("Connection successful!")
        # Create a cursor object to execute SQL queries
        return connection.cursor()


    def test(self):
        try:
            # Connect to PostgreSQL
            connection = psycopg.connect(
                dbname="beerme3",
                user="bob",
                password="admin",
                host="localhost",  # or your database server's IP
                port="5432"  # default PostgreSQL port
            )
            print("Connection successful!")
            # Create a cursor object to execute SQL queries
            self.cursor = connection.cursor()
            # Example query: Fetch PostgreSQL version
            self.cursor.execute("SELECT version();")
            db_version = self.cursor.fetchone()
            print(f"PostgreSQL version: {db_version}")
        except Exception as error:
            print(f"Error connecting to PostgreSQL: {error}")
        finally:
            # Close the connection
            if connection:
                self.cursor.close()
                connection.close()
                print("Connection closed.")


if __name__ == "__main__":
    pg = PostgreSQL()
    pg.test()
    pg.get_cursor()
