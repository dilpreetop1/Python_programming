p1= int(input("enter the price of first product:"))
p2= int(input("enter the price of second product:"))
p3= int(input("enter the price of third product:"))
p4= int(input("enter the price of fourth product:"))
p5= int(input("enter the price of fifth product:")) 
p6= int(input("enter the price of sixth product:"))
p7= int(input("enter the price of seventh product:"))
p8= int(input("enter the price of eight product:"))
p9= int(input("enter the price of ninth product:"))
p10= int(input("enter the price of tenth product:"))

total= p1+p2+p3+p4+p5+p6+p7+p8+p9+p10
disc = (20/100)*total 
finala= total - disc

if total>2000:
    print("discount amount is:",disc)
    print("FINAL AMOUNT IS :", finala)
