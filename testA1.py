from wdp import * 
#bids = load_bids("./bids/bids01.json") # 100 bids
#bids = load_bids("./bids/bids02.json") # 10 bids
#bids = load_bids("./bids/bids03.json") # 100 bids
#bids = load_bids("./bids/bids04.json") # 1000 bids
#bids = load_bids("./bids/bids05.json") # 1000 bids
bids = load_bids("./bids/bids06.json") # 10000 bids

t = timer()
#w = split_wd(bids)
w = winner_determination_v2(bids)
t.stop()
print(bids_sum(w))