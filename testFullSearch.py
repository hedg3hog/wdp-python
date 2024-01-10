from wdp import *
import logging
import pandas as pd

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
logging.basicConfig(filename="FullSearch24.log", format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
logger = logging.getLogger()
ConsoleOutputHandler = logging.StreamHandler()
logger.addHandler(ConsoleOutputHandler)
logger.setLevel(logging.DEBUG)
ConsoleOutputHandler.setFormatter(formatter)



START = 10
END = 100
DATASET_NR = 3
STEP = 1

END = END + 1
i = -1 + DATASET_NR
b = False
for i in range(2,4):
    winners = list()
    times = list()
    bid_sums = list()
    validations = list()
    bundle_sizes = list()
    if b:
        break
    DATASET_NR = i+1
    try:
        all_bids = load_bidsID(f"./bids/bids{(i+1):02}-ID.json")
        logger.info(f"Loaded bids{(i+1):02}.json ({len(all_bids)} bids)")
        for x in range(START,END, STEP):
            bids = all_bids[:x]
            bundle_sizes.append(len(bids))
            print(bundle_sizes[-1])
            t = timer(f"bids{(i+1):02}")
            winners.append(full_search2(bids)[0])
            times.append(t.stop())
            #logger.debug(f"list of winners: {winners[-1]}")
            bid_sums.append(bids_sum(winners[-1]))
            #logger.info(bid_sums[-1])
            validations.append(validate_winners(winners[-1]))
            logger.info(f"Dataset {i+1} ({bundle_sizes[-1]} Bids) finished in {times[-1]} seconds, validation:{validations[-1]}, value:{bid_sums[-1]}")
            if times[-1] > 3600:
                break

    except KeyboardInterrupt:
        logger.info("KeyboardInterrupt")
    b = True


    df =  list()
    for i in range(len(bid_sums)):
        df.append({"datasetsize":bundle_sizes[i], "time":times[i], "value":bid_sums[i], "validation":validations[i]})

    df =  pd.DataFrame(df)
    df.to_csv(f"csv/FS-comp-D{DATASET_NR:02}.csv")
    logger.info(bid_sums)
    logger.info(times)
    logger.info(validations)
    
logger.info("######## END ######### \n")