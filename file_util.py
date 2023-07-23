import csv 


def read_csv(filename):
    # Open the file in read mode
    with open(filename, 'r') as csvfile:
        # Create a CSV DictReader
        reader = csv.DictReader(csvfile)

        # Read each row in the CSV and convert it to a dictionary, then add it to the list
        data = [row for row in reader]
    return data
