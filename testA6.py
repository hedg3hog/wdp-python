from wdp import * 
import logging
import pandas as pd

DATASET_IDS = (3,6,7,12,13) # ids of the datasets to use (1 = bids 01)
#DATASET_IDS = range(1,19)

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
logging.basicConfig(filename="A6-24.log", format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
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

df =  pd.DataFrame(columns=["dataset", "time", "value", "validation"])
for i in range(len(DATASET_IDS)):
   df.append({"dataset":DATASET_IDS[i], "time":times[i], "value":bid_sums[i], "validation":validations[i]}, ignore_index=True)

df.to_csv("A6-24.csv")

logger.info("######## END ######### \n")