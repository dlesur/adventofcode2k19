# Day 5 - Part 1
donnees=input("Entrez les données")
classe=donnees.split(",")
x=0
nbcm=classe[x]



def op1 (mo1, mo2, p1, p2, p3):
    if mo1==0:
        if mo2==0:
            classe[p3]=int(classe[p1])+int(classe[p2])
        else:
            classe[p3]=int(classe[p1])+p2
    else:
        if mo2==0:
            classe[p3]=p1+int(classe[p2])
        else:
            classe[p3]=p1+p2
        

def op2 (mo1, mo2, p1, p2, p3):
    if mo1==0:
        if mo2==0:
            classe[p3]=int(classe[p1])*int(classe[p2])
        else:
            classe[p3]=int(classe[p1])*p2
    else:
        if mo2==0:
            classe[p3]=p1*int(classe[p2])
        else:
            classe[p3]=p1*p2


def op3 (p1):
    classe[p1]=int(input("Op3 : entrer un nb"))


def op4 (mo1, p1):
    if mo1==0:
        print(classe[p1])
    else:
        print(p1)


while nbcm != "99":

    p1=int(classe[x+1])
    p2=int(classe[x+2])
    p3=int(classe[x+3])

    if nbcm=="3":
        op3(p1)
        x=x+2

    else:
        while len(nbcm)!=4:
            nbcm=("0"+nbcm)
        mo1=int(nbcm[1])
        mo2=int(nbcm[0])
        dgop=nbcm[2:]

        if dgop=="01":
            op1(mo1, mo2, p1, p2, p3)
            x=x+4

        elif dgop=="02":
            op2(mo1, mo2, p1, p2, p3)
            x=x+4

        else:
            op4(mo1, p1)
            x=x+2

    nbcm=str(classe[x])

# Yeahhh ! It works but it was a little difficult ! (ok it was very difficult for me !)