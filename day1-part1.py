# Day 1 - Part 1
from math import*


source=open("/home/daphne/Documents/python/puzzle-input.csv", "r")
lines =source.readlines()
source.close
donnees=[0]*len(lines)
x=0
for line in lines:
    donnees[x]=line.rstrip()
    x=x+1


total=0

for loop in range(len(donnees)):
    a=(floor(float(donnees[loop])/3)-2) 
    total=total+a
    b=a

print("here:", total)


#It works