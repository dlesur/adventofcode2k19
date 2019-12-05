# Day 2 - Part 2
donnees=input()
soluce=0
nbtest=0
nbtest2=0


# 1202 program alarm
#classe[1]=12
#classe[2]=2


def op (nb1, nb2, nb3, nb4):
    if nb1==1:
        classe[nb4]=int(classe[nb2])+int(classe[nb3])
    else:
        classe[nb4]=int(classe[nb2])*int(classe[nb3])


while soluce!=19690720:
    x=0
    classe=donnees.split(",")
    classe[1]=nbtest
    classe[2]=nbtest2
    while classe[x] != "99":
        op(int(classe[x]), int(classe[x+1]), int(classe[x+2]), int(classe[x+3]))
        x=x+4
    if nbtest==99:
        nbtest2=nbtest2+1
        nbtest=0
    else:
        nbtest=nbtest+1
    soluce=classe[0]


print(classe[0])
print("here :", classe[1], "and :", classe[2])
print("soluce :", classe[1]*100 + classe[2])