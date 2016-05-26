# detect_unusual_transfers.py

import random
import numpy_wrapper as npw

#############################################################################

BANK_CODES = ["AMERUS33", "CERYUS33", "EQTYUS44",
              "LOYDUS33", "SYNEUS44", "WFBIUS6S"]

BRANCH_IDS = ["125000249", "125000252", "125000371",
              "125000402", "125000596", "125001067"]

#############################################################################

def main():
    """ Our main program.
    """
    # Create 10,000 random transfers.

    days = [1, 2, 3, 4, 5, 6, 7, 8]
    transfers = [] # List of (day, bank_code, branch_id, amount) tuples.

    for i in range(10000):
        day       = random.choice(days)
        bank_code = random.choice(BANK_CODES)
        branch_id = random.choice(BRANCH_IDS)
        amount    = random.randint(1000, 1000000)

        transfers.append((day, bank_code, branch_id, amount))

    # Now process the transfers, grouping them by day and building a NumPy
    # array mapping each branch ID and bank code combination to the total for
    # that branch and bank for that day.

    transfers_by_day = {}
    for day in days:
        transfers_by_day[day] = npw.new(num_rows=len(BANK_CODES),
                                        num_cols=len(BRANCH_IDS))

    for day,bank_code,branch_id,amount in transfers:
        array = transfers_by_day[day]
        row = BRANCH_IDS.index(branch_id)
        col = BANK_CODES.index(bank_code)
        array[row][col] = array[row][col] + amount

    # Get the most recent day.

    latest_day = max(days)

    # Collect the transfers for all days other than the latest one.

    transfers_to_average = []
    for day in days:
        if day != latest_day:
            transfers_to_average.append(transfers_by_day[day])

    # Get the transfers for the current day.

    current = transfers_by_day[latest_day]

    # Calculate the average for each day other than the last one.

    average = npw.average(transfers_to_average)

    # Find the entries in the current day which are more than 150% of the
    # average.

    unusual_transfers = current > average * 1.5

    for row,col in npw.get_indices(unusual_transfers):
        branch_id   = BRANCH_IDS[row]
        bank_code   = BANK_CODES[col]
        average_amt = int(average[row][col])
        current_amt = current[row][col]

        print("Branch {} transferred ${:,d}".format(branch_id,
                                                    current_amt) +
              " to bank {}, average = ${:,d}".format(bank_code,
                                                     average_amt))

#############################################################################

if __name__ == "__main__":
    main()

