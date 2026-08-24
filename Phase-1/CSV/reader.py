import csv
from pathlib import Path

# This tells Python: "Find the folder this script is in"
script_dir = Path(__file__).parent

# This joins that folder path with the CSV file name
file_path = script_dir / 'employees.csv'

with open(file_path, 'r') as file:
    reader=csv.reader(file)
    header=next(reader)
    # print("Collums: ",header)#it will only show header
    for row in reader:
        print(f"name : {row[0]} , dept: {row[2]} ")
 