from wdp import * 
import logging

DATASET_IDS = (10,11,12,13,14,15,16,17,18) # ids of the datasets to use (1 = bids 01)


formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
logging.basicConfig(filename="A6.log", format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
logger = logging.getLogger()
ConsoleOutputHandler = logging.StreamHandler()
logger.addHandler(ConsoleOutputHandler)
logger.setLevel(logging.DEBUG)
ConsoleOutputHandler.setFormatter(formatter)

bid_sums = list()
winners = list()
times = list()
validations = list()

for i in [i-1 for i in DATASET_IDS]:
    bids = load_bids(f"./bids/bids{(i+1):02}.json")#
    logger.info(f"Loaded bids{(i+1):02}.json ({len(bids)} bids)")
    t = timer(f"A3: bids{(i+1):02}")
    winners.append(split_wdp_iterate(bids))
    times.append(t.stop())
    bid_sums.append(bids_sum(winners[-1]))
    #logger.info(bid_sums[-1])
    validations.append(validate_winners(winners[-1]))
    logger.info(f"Dataset {i+1} finished in {times[-1]} seconds, validation:{validations[-1]}, value:{bid_sums[-1]}")


logger.info(bid_sums)
logger.info(times)
logger.info(validations)
logger.info("######## END ######### \n")