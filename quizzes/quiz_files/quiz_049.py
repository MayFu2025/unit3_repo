from quiz_lib import DatabaseWorker

db = DatabaseWorker('bitcoin_exchange.db')

query = "Create table if not exists users (id integer primary key, name text, email text)"
db.run_query(query=query)

query = "Select distinct sender_id, receiver_id from ledger"
db.run_query(query=query)

db.close()