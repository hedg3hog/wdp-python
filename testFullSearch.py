from wdp import *
import logging
import pandas as pd

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
logging.basicConfig(filename="FullSearch.log", format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
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
try:
    all_bids = load_bids(f"./bids/bids{(i+1):02}.json")
    logger.info(f"Loaded bids{(i+1):02}.json ({len(all_bids)} bids)")
    for x in range(10,101):
        bids = all_bids[:x]
        t = timer(f"bids{(i+1):02}")
        winners.append(full_search2(bids)[0])
        times.append(t.stop())
        #logger.debug(f"list of winners: {winners[-1]}")
        bid_sums.append(bids_sum(winners[-1]))
        #logger.info(bid_sums[-1])
        validations.append(validate_winners(winners[-1]))
        logger.info(f"Dataset {i+1} ({x} Bids) finished in {times[-1]} seconds, validation:{validations[-1]}, value:{bid_sums[-1]}")

except KeyboardInterrupt:
    logger.info("KeyboardInterrupt")


df =  list()
for i in range(len(bid_sums)):
   df.append({"dataset":i+10, "time":times[i], "value":bid_sums[i], "validation":validations[i]})

df =  pd.DataFrame(df)
df.to_csv("FS-comp.csv")
logger.info(bid_sums)
logger.info(times)
logger.info(validations)
logger.info("######## END ######### \n")