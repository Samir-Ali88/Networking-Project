import csv

with open('CSV/employees.csv','r') as file:
    reader=csv.DictReader(file)
    for row in reader:
        name=row['Name']
        salary=int(row['Salary'])
        print(f"Nmae is : {name} his salary is {salary}")