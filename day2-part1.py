# Day 2 - Part 1
donnees=input()
classe=donnees.split(",")
nb=0
x=0


# 1202 program alarm
classe[1]=12
classe[2]=2


def op (nb1, nb2, nb3, nb4):
    if nb1==1:
        classe[nb4]=int(classe[nb2])+int(classe[nb3])
    else:
        classe[nb4]=int(classe[nb2])*int(classe[nb3])


while classe[x] != "99":
    op(int(classe[x]), int(classe[x+1]), int(classe[x+2]), int(classe[x+3]))
    x=x+4


print("here :", classe[0])
