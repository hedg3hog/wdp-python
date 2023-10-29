from wdp import * 
import logging

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
logging.basicConfig(filename="A2.log", format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
logger = logging.getLogger()
ConsoleOutputHandler = logging.StreamHandler()
logger.addHandler(ConsoleOutputHandler)
logger.setLevel(logging.DEBUG)
ConsoleOutputHandler.setFormatter(formatter)

bid_sums = list()
winners = list()
times = list()
validations = list()

for i in range(2):
    bids = load_bids(f"./bids/bids{(i+1):02}.json")
    logger.info(f"Loaded bids{(i+1):02}.json")
    t = timer(f"A3: bids{(i+1):02}")
    winners.append(winner_determination_v2(bids))
    times.append(t.stop())
    bid_sums.append(bids_sum(winners[i]))
    logger.info(bid_sums[i])
    validations.append(validate_winners(winners[i]))
    logger.info(f"Dataset {i+1} finished in {times[-1]} seconds, validation:{validations[-1]}, value:{bid_sums[-1]}")

logger.info(bid_sums)
logger.info(times)
logger.info(validations)
