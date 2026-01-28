def plus_grand(a,b,c):
    if a>=b and a>=c:
        print("Le plus grand est",a)
    elif b>=a and b>=c:
        print("Le plus grand est",b)
    else:
        print("Le plus grand est",c)

def programme_1():
    for i in range(0,11):
        print(i, end=' ')

def programme_2():
    myst=1
    a=int(input("Entrez un nombre : "))
    b=int(input("Entrez un deuxième nombre : "))
    if b<0:
        n = -b
    else :
        n = b
    
    while n>0:
        myst = myst * a
        n = n - 1
    if b<0:
        myst = 1/myst
    print("Il y a",myst)

def programme_3():
    a=int(input("Entrez un nombre pour a "))
    print(f"E0 \t {a}") #E0
    b=int(input("Entrez un nombre pour b "))
    print(f"E1 \t {a} {b}") #E1
    a=a+b
    print(f"E2 \t {a} {b}") #E2
    b=a-b
    print(f"E3 \t {a} {b}") #E3
    a=a-b
    print(f"E4 \t {a} {b}") #E4


def programme_4():
    a=3
    b=8
    if b>=10:
        b=b*a
        a=b
    c=a+b
    return c

def programme_5():
    myst=0
    a=int(input("Entrez un nombre : "))
    b=int(input("Entrez un deuxième nombre : "))
    if b>0:
        n=b
    else:
        n=-b
    
    while n>0:
        myst = myst + a
        n=n-1
        if b<0:
            myst = -myst
        print(a, "op",b, "=", myst)

programme_5()