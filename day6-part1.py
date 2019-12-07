# Day 6 - Part 1

source=open("/home/daphne/Documents/python/puzzle6.csv", "r")
lines =source.readlines()
source.close
donnees=[0]*len(lines)
x=0
for line in lines:
    donnees[x]=line.rstrip()
    x=x+1


orbites=["COM"]*1
newel=1
prel=0
total=0
for b in range(len(donnees)):
    new=0
    for loop in range(len(donnees)):
        case=donnees[loop]
        obj=case[0:3]
        for i in range(newel):
            if obj==orbites[prel+i]:
                orbites.append(case[4:])
                total=total+1+b
                new=new+1

    prel=len(orbites)-new
    newel=new


print("here:", total)

