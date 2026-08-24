import csv
data=[
{ "username":"samir","pass":123},
{"username": "sahion", "pass":"234"} ,
{"username": "admin", "pass": "admin123"},
{"username": "john", "pass": "qwerty"},
]
names=["username","pass"]
with open('CSV/scan_results.csv','w',newline='') as infile:
    writer=csv.DictWriter(infile,fieldnames=names)
    writer.writeheader()
    writer.writerows(data)

with open('CSV/scan_results.csv','r',newline='') as infile:
    reader=csv.DictReader(infile)
    for row in reader:
        print(f"username {row["username"]} and passs is : {row["pass"]}")