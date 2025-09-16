unit = int(input("enter the number of units:"))
if unit<=100:
    bill = unit*2
    print("bill is", bill)
elif unit>100 and unit <=200:
    bill = unit*3
    print("BILL is", bill)
elif unit>200 and unit<=249:
    bill = unit*4
    print("Bill is", bill)
elif unit>=250 and unit<=300:
    bill= unit*5
    disc = 5/100*bill
    finalbill= bill-disc
    print("discounted amount is", disc)
    print("the amount after discount is ", finalbill)