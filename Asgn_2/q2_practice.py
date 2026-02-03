import csv
import json

def mean(c,d):
    m=c/d
    return m

c=0
d=0
Max_Temp = 0
Min_Temp = 35
with open("sample/stat.csv") as f:
    a=csv.DictReader(f)
    #for r in a:
    #            print(r)
    #Captures Column Field Dynamically
    columns=a.fieldnames
    #print(columns)
    #for r in a:
    #    for c in columns:
    #        print(r,c)

    #rows = list(a)
    # Assuming 'rows' is your list of dicts from list(reader)
    #if rows:
    #    columns = list(rows[0].keys())
    #    row = list(rows[1].values())
        #print(row)
        #print(columns)

    #Count Mean Maximum Minimum
    for r in a:
        a=int(r["temperature"])
        if a > Max_Temp:
            Max_Temp = a
        if a < Min_Temp:
            Min_Temp= a
        c=c+int(r['temperature'])
        d=d+1
        l=mean(c,d)
    print("total_temp:",c,"Mean_temp",l,"Minimum",Min_Temp,"Maximum",Max_Temp)
    
    with open("q2.json","w") as j:
        summary= {"col": r ,"total " : c ," mean" : l,"min": Min_Temp,"max" : Max_Temp}
        json.dump(summary,j)
