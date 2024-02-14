from quiz_lib import DatabaseWorker, check_text

db = DatabaseWorker(name='bitcoin_exchange.db')
query = "Select * from ledger"
result = db.search(query=query, multiple=True)
# print(result)

for n in result:
    pre_hash = f"id {n[0]},sender_id {n[1]},receiver_id {n[2]},amount {n[3]}"
    if check_text(hashed=n[4], text=pre_hash):
        print(f"Tx(id={n[0]}) Signature Matches")
    else:
        print(f"Tx(id={n[0]}) Error Signature")