import sqlite3
from passlib.hash import sha256_crypt

class DatabaseWorker:
    def __init__(self, name:str):
        self.name_db = name

        # Step 1: Create a connection
        self.connection = sqlite3.connect(self.name_db)
        # Step 2: Set cursor/where it inputs into table
        self.cursor = self.connection.cursor()

    def run_query(self, query:str):
        self.cursor.execute(query)  # Run query
        self.connection.commit()  # Save changes

    def insert(self, query:str):
        self.run_query(query)

    def search(self, query:str, multiple:bool = False):
        results = self.cursor.execute(query)
        self.run_query(query)
        if multiple:
            return results.fetchall()  # Fetchall returns multiple rows
        else:
            return results.fetchone()  # Fetchone returns single value

    def close(self):
        self.connection.close()


hasher = sha256_crypt.using(rounds=30000)
def make_hash(text: str) -> str:
    return hasher.hash(text)

def check_text(hashed: str, text: str) -> bool:
    return hasher.verify(text, hashed)
