import csv
import json
l=[]
u=[]
s={}
with open("sample/ledger.txt","r") as f:
    #a=f.read()
    #b=f.readline()
    #f.split(",").strip()
    #for a in f:
    #  print(a)
    for line in f:
        parts=line.split(",")
        i=parts[0].strip()
        u=parts[1].strip()
        a=parts[2].strip()

        if i not in s:
            s[a]=[]
#Printing the results:

for a in s:
    print(a)
