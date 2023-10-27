import random
import json

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

def save_bids(number_of_bids, items, max_items, bid_file):
    bids = gen_bids(number_of_bids, items, max_items_per_bid=max_items)

    bidString = json.dumps(bids)

    f = open(bid_file, "w")
    f.write(bidString)
    f.close()

if __name__ == "__main__":
    f = open("./items/items1000.json")
    items1 = json.loads(f.read())
    f.close

    save_bids(100, items1[:10], 10, "./bids/bids-10items-max10-100-01")