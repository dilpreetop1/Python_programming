s = input("select the seat" + "\n" + "a.classic@rs100"+"\n"+"b.premium@rs300"+"\n"+"c.recliner@rs500"+"\n")
n = int(input("enter the numer of seats"))
#a= 100
#b= 300
#c= 500
if s=='a':
    amount = n*100
    print(amount)
    if amount>=500 and amount<1500:
        u = input("hurray u got meal worth rs 200 or 2 percent discount:"+"\n"+ "choose a for meal and b for discount:")
    if u =="a":
        print("u got free meal")
    else:
        print("u got dsicount")
    if amount>1500:
        u= input("hurray u got meal worth rs 500 or 4 percent discount:"+"\n"+ "choose a for meal and b for discount:")
    if u=="a":
         print("u got free meal")
    else:
        print("u got dsicount")


        

elif s=='b':
    amount= n*300
    print(amount)
#else:
    #amount= n+c
#n = int(input("enter the number of seats:"))
#amount = x+n

#if amount>=500 and amount<1500:
    #u= input("hurray u got meal worth rs 200 or 2 percent discount:"+"\n"+ "choose a for meal and b for discount:")
    
    '''if u=="a":
        print("u got free meal")
    else:
        print("u got dsicount")

elif amount>=1500:
    p= input("hurray u got meal worth rs 500 or 4 percent discount"+"\n"+ "choose a for meal"+"\n"+"and b for discount")
    if p=="a":
        print("u got free meal")
        
    else:
        print("u got discount")'''