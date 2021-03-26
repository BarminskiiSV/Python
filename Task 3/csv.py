import random
raz = 10
k = ''

d1 = random.randint(5, 10000000)
d2 = random.randint(5, d1)
n ="META DATA:\n"+str(d1)+"(объем бочки)\n" + str(d2) + "(текущий объем воды в бочке)\n"


for i in range(0, raz):
    c = random.randint(0, 1)
    if c == 0:
        s2 = "успех"
    elif c == 1:
        s2 = "фейл"

    c = random.randint(0, 1)
    if c == 0:
        s3 = "top up"
    elif c == 1:
        s3 = "scoop"

    c1 = random.randint(0, 20)
    if c1 < 10:
        c1 = "0" + str(c1)
    c1 = str(c1)

    c2 = random.randint(1, 12)
    if c2 < 10:
        c2 = "0" + str(c2)
    c2 = str(c2)

    c3 = random.randint(1, 30)
    if c3 < 10:
        c3 = "0" + str(c3)
    c3 = str(c3)

    c4 = random.randint(0, 23)
    if c4 < 10:
        c4 = "0" + str(c4)
    c4 = str(c4)

    c5 = random.randint(0, 59)
    if c5 < 10:
        c5 = "0" + str(c5)
    c5 = str(c5)

    c6 = random.randint(0, 59)
    if c6 < 10:
        c6 = "0" + str(c6)
    c6 = str(c6)
    k += "20"+c1+"-"+c2+"-"+c3+"Т"+c4+":"+c5+":"+c6+".124Z" + "– [username1] - wanna "+s3+" "+str(random.randint(1, 50))+"l ("+s2+")\n" 


log = n + k