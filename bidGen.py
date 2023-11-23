import random
import json
import pandas as pd

def gen_bids(n, items, max_items_per_bid=None):
    "returns a list of n bid lists ((item_choice), value)"
    bids = list()
    if not max_items_per_bid:
        max_items_per_bid=len(items)
    for _ in range(n):
        chosen_items = random.sample(items, random.randint(1,max_items_per_bid))
        value = sum([random.randint(1,100) for _ in chosen_items])
        bids.append((chosen_items, value))
    return bids

 
def load_items(item_file):
    f = open(item_file, "r")
    items = json.loads(f.read())
    f.close()
    return items

def save_bids(number_of_bids, items, max_items, bid_file):
    bids = gen_bids(number_of_bids, items, max_items_per_bid=max_items)

    bidString = json.dumps(bids)

    f = open(bid_file, "w")
    f.write(bidString)
    f.close()

if __name__ == "__main__":
    f = open("./items/items1000.json")
    items1 = json.loads(f.read())
    print(len(items1))
    f.close
    
    l = list()
    x = 20
    for anz_i in range(10,21):
        for max_i in range(2,min(16, anz_i), 2):
            l.append((x,70,anz_i,max_i))
            x+=1

    
    for i in l:
       save_bids(i[1], range(i[2]), i[3], f"./bids2/comp-bids{i[0]}.json")

    df = pd.DataFrame(l)
    df.to_csv("bids2/bids2.csv")

    