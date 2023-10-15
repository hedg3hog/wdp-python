import random
# G = Bid Graph
def gen_bids(n, items):
    "returns a list of n bid tuples ((item_choice), value)"
    bids = list()
    for i in range(n):
        chosen_items = random.sample(items, random.randint(1,len(items)))
        chosen_items.sort()
        set(chosen_items)
        value = len(chosen_items) * random.randint(1,20)
        bids.append((chosen_items, value))
    return bids

class BidGraph:
    def __init__(self):
        pass
        
    

def bob(G,g,MIN):
    pass

items = ("a", "b", "c", "d", "e", "f")

bids = gen_bids(10, items)
print(bids)