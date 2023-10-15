import random
# G = Bid Graph
def gen_bids(n, items, max_items_per_bid=None):
    "returns a list of n bid tuples ((item_choice), value)"
    bids = list()
    if not max_items_per_bid:
        max_items_per_bid=len(items)
    for i in range(n):
        chosen_items = random.sample(items, random.randint(1,max_items_per_bid))
        chosen_items = set(sorted(chosen_items))
        value = len(chosen_items) * random.randint(1,10)
        bids.append((chosen_items, value))
    return bids


def winner_determination(bids:list):
    """hopefully solves wdp, takes maybe long"""
    bids = sorted(bids, key= lambda bid: -bid[1]) # highest to lowest bid
    f = 0 # highest revenue
    h_path = list() # path of highest revenue
    x = 0 # current first item

    while x < len(bids)/2 + 1:
        c_path = list() # current path
        c_bids = bids[x:] # bids currently active
        c_sum = 0 # current summ
        c_remaining = bids_sum(c_bids) # highest remaining bids can contribute
        for i,b in enumerate(c_bids):
            if bid_available(b, c_path):
                c_path.append(b)
                c_sum += b[1]
                if c_sum > f:
                    f = c_sum
                    h_path = c_path
                c_remaining -= b[1]
                if (c_sum + c_remaining) < f:
                    break
        x +=1
    




    return h_path
class BidGraph:
    def __init__(self):
        pass
        
        
        
def prune_bids(bids:list, path):
    """Returns only bids with items that are not already taken"""
    s = set()
    for b in path:
        s = s.union(b[0])
    
    prune = list()
    for i,b in enumerate(bids):
        if s.intersection(b[0]):
            prune.append(i)
    
    for i in prune[::-1]:
        bids.pop(i)
    return bids

def bid_available(bid:tuple, path:list) -> bool:
    s = set()
    for b in path:
        s = s.union(b[0])
    return not s.intersection(bid[0])

def bids_sum(bids:list):
    s = 0
    for b in bids:
        s += b[1]
    return s
    

def bob(G,g,MIN):
    pass

items = ("a", "b", "c", "d", "e", "f")

bids = gen_bids(10, items, max_items_per_bid=3)
#bids = [({'e'}, 7), ({'d'}, 8), ({'b'}, 3), ({'f', 'e', 'd', 'c', 'a', 'b'}, 54), ({'f', 'd', 'c', 'a', 'b'}, 35), ({'f', 'e', 'd', 'c', 'a', 'b'}, 12), ({'b'}, 6), ({'c', 'b', 'd', 'a'}, 12), ({'f', 'e', 'd', 'c', 'b'}, 30), ({'b'}, 3), ({'b', 'f'}, 2), ({'e'}, 4), ({'f', 'e', 'd', 'a', 'b'}, 45), ({'e', 'b', 'd', 'f'}, 24), ({'f', 'e', 'd', 'a', 'b'}, 10), ({'b', 'd', 'c'}, 27), ({'f', 'e', 'd', 'c', 'b'}, 5), ({'c', 'b', 'd', 'a'}, 16), ({'f', 'e', 'd', 'c', 'a', 'b'}, 60), ({'e', 'f'}, 4), ({'e', 'f', 'd', 'c'}, 32), ({'d'}, 2), ({'e', 'd', 'a'}, 9), ({'f', 'd', 'c', 'a', 'b'}, 35), ({'f', 'e', 'c', 'a', 'b'}, 45), ({'c', 'a', 'e'}, 12), ({'e', 'b', 'a'}, 18), ({'c'}, 10), ({'a'}, 10), ({'c', 'b', 'a', 'f'}, 28), ({'e'}, 1), ({'f', 'e', 'd', 'a', 'b'}, 50), ({'e', 'd'}, 2), ({'f', 'd', 'c', 'a', 'b'}, 40), ({'f', 'e', 'd', 'c', 'a', 'b'}, 60), ({'f'}, 4), ({'e', 'b', 'd', 'c'}, 24), ({'e', 'f', 'a'}, 27), ({'e', 'd', 'c', 'a', 'b'}, 40), ({'e', 'f', 'a'}, 9), ({'c', 'f', 'a'}, 12), ({'c'}, 9), ({'b', 'd', 'f'}, 18), ({'e', 'f', 'd'}, 18), ({'e'}, 5), ({'f', 'e', 'd', 'c', 'a', 'b'}, 36), ({'b', 'c'}, 8), ({'f', 'e', 'd', 'c', 'a', 'b'}, 54), ({'b', 'd', 'c', 'f'}, 28), ({'d', 'c'}, 2), ({'b', 'd', 'c', 'f'}, 12), ({'b', 'd', 'a'}, 12), ({'e', 'b', 'd', 'a'}, 28), ({'f', 'e', 'd', 'c', 'a', 'b'}, 6), ({'f', 'e', 'd', 'c', 'b'}, 45), ({'c'}, 3), ({'e', 'd', 'c', 'a', 'b'}, 40), ({'c', 'd', 'a', 'e'}, 24), ({'e', 'b'}, 16), ({'f', 'e', 'd', 'c', 'a', 'b'}, 48), ({'f', 'e', 'd', 'c', 'a', 'b'}, 36), ({'f', 'd'}, 14), ({'c', 'd', 'a', 'e'}, 16), ({'b', 'd', 'a', 'f'}, 28), ({'e', 'a'}, 6), ({'f', 'e', 'd', 'c', 'a', 'b'}, 36), ({'f', 'e', 'd', 'a', 'b'}, 10), ({'f', 'e', 'd', 'c', 'b'}, 30), ({'a'}, 9), ({'e', 'd', 'c', 'a', 'b'}, 5), ({'b', 'a', 'f'}, 12), ({'b', 'd', 'c'}, 9), ({'c', 'a'}, 18), ({'a'}, 5), ({'c', 'd', 'a'}, 30), ({'f', 'e', 'd', 'c', 'a', 'b'}, 6), ({'f', 'e', 'd', 'c', 'a', 'b'}, 6), ({'f', 'e', 'd', 'a', 'b'}, 5), ({'e'}, 4), ({'e', 'f', 'd', 'c'}, 8), ({'b', 'd', 'c'}, 15), ({'b'}, 7), ({'e'}, 9), ({'f', 'e', 'd', 'c', 'a', 'b'}, 18), ({'b', 'f'}, 18), ({'f', 'e', 'd', 'a', 'b'}, 25), ({'a'}, 1), ({'e', 'b', 'd', 'c'}, 24), ({'f'}, 1), ({'f', 'e', 'd', 'c', 'a'}, 50), ({'e', 'a'}, 2), ({'e', 'f', 'c'}, 15), ({'c', 'f', 'a'}, 15), ({'f', 'e', 'd', 'a', 'b'}, 25), ({'f'}, 1), ({'f', 'd', 'c', 'a', 'b'}, 20), ({'f'}, 1), ({'f', 'e', 'd', 'c', 'a'}, 50), ({'c', 'f', 'a'}, 24), ({'f', 'd', 'c', 'a', 'b'}, 30)] 
#print(bids, "\n")
print(winner_determination(bids))