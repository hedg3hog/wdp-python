from wdp import * 

bid_sums = list()
winners = list()
times = list()

for i in range(6):
    bids = load_bids(f"./bids/bids{(i+1):02}.json")
    print(f"Loaded bids{(i+1):02}.json")
    t = timer(f"A3: bids{(i+1):02}")
    winners.append(winner_determination_v2(bids))
    times.append(t.stop())
    bid_sums.append(bids_sum(winners[i]))
    print(bid_sums[i])

print(bid_sums)
print(times)