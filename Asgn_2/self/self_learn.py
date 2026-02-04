# File Handling in Python

'''a+=append+read, r=read ,r+=read write ,a= append,write overwrites the file 

path="test.txt"
file=open(path,"a+")
file.seek(0)
contents=file.read()
print("before :",contents)
#file.close()
#writing in a file
file.write("this is forth line \n this is fifth line")
file.seek(0)
c=file.read()
print("after :", c)
file.close()

##
with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")

#open and read the file after the appending:
with open("demofile.txt") as f:
  print(f.read())
'''



