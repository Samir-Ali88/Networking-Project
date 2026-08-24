import csv
updated_data=[]
with open('CSV/employees.csv','r') as infile:
    reader=csv.DictReader(infile)
    headers=reader.fieldnames
    for row in reader:
        if row['Department']=='IT':
            salary=int(row['Salary'])
            new_salary=int(salary*1.10)
            row['Salary']=str(new_salary
            )
        updated_data.append(row)

with open('CSV/updated_employees.csv','w',newline='') as outfile:
    writer=csv.DictWriter(outfile,fieldnames=headers)
    writer.writeheader()
    writer.writerows(updated_data)

print("Everything updated suceccfully")    