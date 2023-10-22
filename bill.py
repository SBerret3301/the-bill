# Algorihme Bill
# variables
#      b , c , d , e , l ,m , p : reel  
#      a , x , y , z : chaine de caracter
#      n : entier
# Debut
#    pour i<--1 a 3 faire
#    |   Ecrire("enter the name of the customer n'",i,":")
#    |   Lire(a)
#    |   Ecrire("enter the number of items : ")
#    |   Lire(n)
#    |   pour j<--1 a n faire
#    |   |  Ecrire("Give the price of the item n'",j,":")
#    |   |  Lire(b)
#    |   |  si i = 1 alors
#    |   |  |   c = b + b * 0.15 - b * 0.02 
#    |   |  |   l<-- l + c
#    |   |  |   x = a
#    |   |  sinon
#    |   |  |  si i = 2 alors
#    |   |  |  |    d = b + b * 0.15 - b * 0.02
#    |   |  |  |    m<-- m + d
#    |   |  |  |    y = a
#    |   |  |  sinon
#    |   |  |  |  si i = 3 alors
#    |   |  |  |  |   e = b + b * 0.15 - b * 0.02
#    |   |  |  |  |   p<-- p + e 
#    |   |  |  |  |   z = a
#    |   |  |  |  Finsi
#    |   |  |  Finsi
#    |   |  Finsi
#    |   Finpour
#    Finpour
#    Ecrire("The Total to be paid for the customer",x,":",l,"DH")
#    Ecrire("The Total to be paid for the customer",y,":",m,"DH")
#    Ecrire("The Total to be paid for the customer",z,":",p,"DH")
# Fin


l = 0
m = 0
p = 0
for i in range(3):
    print("enter the name of the customer n'",i+1,":")
    a = input()
    n = int(input("enter the number of items : "))
    for j in range(n):
        print("Give the price of the item n'",j+1,":")
        b = float(input())
        if i == 0 :
            x = a
            c = b + b * 0.15 - b * 0.02
            l += c
        if i == 1 :
            d = b + b * 0.15 - b * 0.02
            m += d
            y = a
        if i == 2 :
            e = b + b * 0.15 - b * 0.02
            p += e
            z = a
print("The Total to be paid for the customer",x,":",l,"DH")
print("The Total to be paid for the customer",y,":",m,"DH")
print("The Total to be paid for the customer",z,":",p,"DH")
