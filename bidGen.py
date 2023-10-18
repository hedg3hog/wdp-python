import random
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