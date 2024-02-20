# Quiz 048
<hr>

### Prompt
![](images/quiz_048_slide.png)
*fig. 1* **Screenshot of quiz slides**

### Solution
```.py
from quiz_lib import DatabaseWorker, check_text, make_hash

db = DatabaseWorker(name='bitcoin_exchange.db')
query = "Select * from ledger"
result = db.search(query=query, multiple=True)

total = 0
for n in result:
    pre_hash = f"id {n[0]},sender_id {n[1]},receiver_id {n[2]},amount {n[3]}"
    if check_text(hashed=n[4], text=pre_hash):
        total += n[3]

print(total)
```

### Evidence
![](images/quiz_048_evidence.png)
*fig. 2* **Screenshot of output in console**

### ER Diagram
![](images/quiz_047_diagram.png)
*fig. 3* **ER Diagram for `bitcoin_exchange.db`**