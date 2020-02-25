#!/bin/activate python
import csv
from datetime import datetime
from datetime import date as date_class

# CONFIGURATION
INPUT_DIR = 'input/'                            # Relative to this file
INPUT_FILES = ['data_1.csv', 'data_2.csv']      # 2 files inside INPUT_DIR

OUTPUT_DIR = 'output/'                          # Relative to this file
OUTPUT_FILE = 'output.csv'

SIG_DIGS = 2                                    # Number of significant digits to found floats to
OUTPUT_DATE_FORMAT = '%m/%d/%Y'                 # How you want the output date to be formatted

# SCRIPT
try:
    with open(INPUT_DIR + INPUT_FILES[0], mode='r') as f1,\
            open(INPUT_DIR + INPUT_FILES[1], mode='r') as f2,\
            open(OUTPUT_DIR + OUTPUT_FILE, mode='w') as output:

        input_1 = csv.reader(f1, delimiter=',')
        input_2 = csv.reader(f2, delimiter=',')
        output = csv.writer(output)
        next(input_1)                                               # skip header lines
        next(input_2)                                               # skip header lines
        output.writerow(['item_identifier', 'result', 'date', 'new_value'])    # write output header

        def calculate_row(previous, current, next):
            """
            Helper function to calculate the row to write based on previous,
            current, and next rows.
            Previous and next rows can be None
            """

            item_identifier = current[0]
            result = round(number=float(current[1]) * float(current[4]),
                           ndigits=SIG_DIGS)
            try:
                date_split = datetime.strptime(current[5], '%m/%d/%Y')
            except ValueError:
                date_split = datetime.strptime(current[5], '%Y-%m-%dT%H:%M:%S')

            date = date_class(year=int(date_split.year),
                              month=int(date_split.month),
                              day=int(date_split.day))

            if previous is not None and previous[2]:
                new_value = previous[2]
            elif previous is not None and next is not None and previous[2] and next[2]:
                new_value = round(number=(float(previous[2]) / float(next[2]))/2, ndigits=SIG_DIGS)
            else:
                new_value = 1

            return [str(item_identifier), str(result), str(date.strftime(OUTPUT_DATE_FORMAT)), str(new_value)]

        previous_row = None
        current_row = None
        next_row = None

        for row_1, row_2 in zip(input_1, input_2):
            # Update rows!
            previous_row = current_row
            current_row = next_row
            next_row = row_1 + row_2

            # Perform logic!
            if current_row is not None:
                row_to_write = calculate_row(previous=previous_row,
                                             current=current_row,
                                             next=next_row)

                output.writerow(row_to_write)

        # Write final row
        row_to_write = calculate_row(previous=current_row,
                                     current=next_row,
                                     next=None)

        output.writerow(row_to_write)

except FileNotFoundError as e:
    print(f"Input directory or input file `{e.filename}` doesn't exist!")
