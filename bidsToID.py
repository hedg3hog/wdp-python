import json
from wdp import *


f = open("./items/items1000.json")
items = json.loads(f.read())
f.close()

for i in range(0,19):
    print("Bids", 1+i)
    bids = load_bids(f"./bids/bids{(i+1):02}.json")

    l = list()

    for b in bids:
        l.append({"items": [items.index(s) for s in b[0]], "value": b[1]})
        
    j = json.dumps(l)

    f = open(f"./bids/bids{(i+1):02}-ID.json", "w")
    f.write(j)
    f.close()  
    

        

