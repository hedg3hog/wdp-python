import json
import time
from tqdm import tqdm


def winner_determination(bids:list):
    """hopefully solves wdp, takes maybe long"""
    bids = sorted(bids, key= lambda bid: -bid[1]) # highest to lowest bid
    f = 0 # highest revenue
    h_path = list() # path of highest revenue
    x = 0 # current first item

    for x in tqdm(range(len(bids))): # TODO: change to full list
        c_path = list() # current path
        c_bids = bids[x:] # bids currently active
        c_sum = 0 # current summ
        c_remaining = bids_sum(c_bids) # highest remaining bids can contribute
        for b in c_bids:
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


def winner_determination_old(bids:list):
    """hopefully solves wdp, takes maybe long"""
    bids = sorted(bids, key= lambda bid: -bid[1]) # highest to lowest bid
    f = 0 # highest revenue
    h_path = list() # path of highest revenue
    x = 0 # current first item

    for x in tqdm(range(len(bids) // 2 + 1)): # 
        c_path = list() # current path
        c_bids = bids[x:] # bids currently active
        c_sum = 0 # current summ
        c_remaining = bids_sum(c_bids) # highest remaining bids can contribute
        for b in c_bids:
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
        
        
        
def prune_bids(bids:list, path):
    """Returns only bids with items that are not already taken"""
    bids = bids.copy()
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
    
def load_bids(filename):
    with open(filename, "r") as f:
        s = f.read()
        f.close()
    bids = json.loads(s)
    for i in range(len(bids)):
        bids[i] = (set(bids[i][0]), bids[i][1])

    return bids

def benchmark_wd(bids):
    t = time.time()
    w = winner_determination(bids)
    t = (time.time()-t)
    t = round(t, ndigits=4)

    return w, t


class timer():
    def __init__(self, name="timer") -> None:
        self.timer = time.time()
        self.name = name
    
    def start(self):
        self.timer = time.time()
        print(f"{self.name} started")

    def stop(self):
        if self.timer == 0:
            print(f"{self.name} already stopped")
            return 0
        t = (time.time()-self.timer)
        t = round(t, ndigits=4)
        print(f"{self.name} stopped after {t} seconds")
        self.timer = 0
        return t

    def time(self):
        t = (time.time()-self.timer)
        t = round(t, ndigits=4)
        print(f"{self.name} running: {t} seconds")
        return t



def split_wd(bids):
    winner_list = list()
    for i in range(0, len(bids), 200):
        x = min(i + 200, len(bids))
        winner_list += winner_determination(bids[i:x])
   
    winner_list = winner_determination(winner_list)
    bids_new = prune_bids(bids.copy(), winner_list)
    winner_list = winner_determination(winner_list + bids_new)

    return winner_list

def winner_determination_v2(bids):
    bids = sorted(bids, key= lambda bid: -bid[1]) # highest to lowest bid
    f = 0 # highest revenue
    h_path = list() # path of highest revenue
    x = 0 # current first item

    for x in tqdm(range(len(bids) // 2 + 1)): # 
        c_path = list() # current path
        c_bids = bids[x:] # bids currently active
        c_sum = 0 # current summ
        c_remaining = bids_sum(c_bids) # highest remaining bids can contribute
        for b in c_bids:
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


#bids1 = load_bids("./bids/bids01.json") # 100 bids
#bids2 = load_bids("./bids/bids02.json") # 10 bids
#bids3 = load_bids("./bids/bids03.json") # 100 bids
#bids4 = load_bids("./bids/bids04.json") # 1000 bids
#bids5 = load_bids("./bids/bids05.json") # 1000 bids
#bids6 = load_bids("./bids/bids06.json") # 10000 bids





#print(winner_determination(bids5) == winner_determination_old(bids5))

