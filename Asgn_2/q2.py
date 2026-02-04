import csv

with open("sample/stat.csv", mode="r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
#    print(rows)
# To see a specific value (e.g., a column named 'Age' in the first row):
#if rows:
#    print(f"The first entry's age is: {rows[0]['Age']}")

# To iterate through everything:
#for row in rows:
   # print(row)
#Dynamically determine column names
    columns = reader.fieldnames
    #print(columns)

    for row in reader:
        for col in columns:
            print(row,col)
