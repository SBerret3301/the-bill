# Algorihme Bill
# variables
#      b , c , d , e : chaine de caracter 
#      a , x , y , z : reel
# Debut
#    pour i<--1 a 3 faire
#    |   Ecrire("enter the name of the customer n'",i+1,":")
#    |   Lire(a)
#    |   Ecrire("Give the price of the item :")
#    |   Lire(b)
#    |   si i = 1 alors
#    |   |   c = b + b * 0.15 - b * 0.02 
#    |   |   x = a
#    |   sinon
#    |   |  si i = 2 alors
#    |   |  |    d = b + b * 0.15 - b * 0.02 
#    |   |  |    y = a
#    |   |  sinon
#    |   |  |  si i = 3 alors
#    |   |  |  |   e = b + b * 0.15 - b * 0.02 
#    |   |  |  |   z = a
#    |   |  |  Finsi
#    |   |  Finsi
#    |   Finsi
#    Finpour
#    Ecrire("The Total to be paid for the customer",x,":",c,"DH")
#    Ecrire("The Total to be paid for the customer",y,":",d,"DH")
#    Ecrire("The Total to be paid for the customer",z,":",e,"DH")
# Fin



for i in range(3):
    print("enter the name of the customer n'",i+1,":")
    a = input()
    b = int(input("Give the price of the item :"))
    if i == 0 :
        c = b + b * 0.15 - b * 0.02 
        x = a
    if i == 1 :
        d = b + b * 0.15 - b * 0.02
        y = a
    if i == 2 :
        e = b + b * 0.15 - b * 0.02
        z = a
print("The Total to be paid for the customer",x,":",c,"DH")
print("The Total to be paid for the customer",y,":",d,"DH")
print("The Total to be paid for the customer",z,":",e,"DH")
