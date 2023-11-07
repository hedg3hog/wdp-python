from wdp import *
import logging

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
logging.basicConfig(filename="A6.log", format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
logger = logging.getLogger()
ConsoleOutputHandler = logging.StreamHandler()
logger.addHandler(ConsoleOutputHandler)
logger.setLevel(logging.DEBUG)
ConsoleOutputHandler.setFormatter(formatter)

winners = list()
times = list()
bid_sums = list()
validations = list()

i = -1 + 3

bids = load_bids(f"./bids/bids{(i+1):02}.json")
logger.info(f"Loaded bids{(i+1):02}.json ({len(bids)} bids)")
t = timer(f"A3: bids{(i+1):02}")
winners.append(full_search(bids)[0])
times.append(t.stop())
logger.debug(f"list of winners: {winners[-1]}")
bid_sums.append(bids_sum(winners[-1]))
#logger.info(bid_sums[-1])
validations.append(validate_winners(winners[-1]))
logger.info(f"Dataset {i+1} finished in {times[-1]} seconds, validation:{validations[-1]}, value:{bid_sums[-1]}")

print(f"Dataset {i+1} finished in {times[-1]} seconds, validation:{validations[-1]}, value:{bid_sums[-1]}")