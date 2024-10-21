import json
import csv

# Convert CSV data from 'dataset/dataset.csv' file to JSON format and write to file
submission = [
    # Write your JSON formatted data here

]

with open("submission.json","w") as file:
    reader = csv.DictReader(file)
    rows = list(reader)
    print(rows)
    json.dump(submission, file, indent = 4)