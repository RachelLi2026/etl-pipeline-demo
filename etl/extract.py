import csv

def extract_data(path='data/input.csv'):
    rows = []
    with open(path, mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    ## This changes are done to test feature extract step branch.
    ## This is second change done to test feature extract step branch.
    return rows