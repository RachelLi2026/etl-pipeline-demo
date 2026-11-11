import csv

def extract_data(path='data/input.csv'):
    rows = []
    with open(path, mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows