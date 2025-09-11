s1= int(input("enter the marks of subject 1:"))
s2= int(input("enter the marks of subject 2:"))
s3= int(input("enter the marks of subject 3:"))
s4= int(input("enter the marks of subject 4:"))
s5= int(input("enter the marks of subject 5:"))

total= s1+s2+s3+s4+s5
Percentage= (total / 500) * 100
print(Percentage)

if Percentage>=50:
    print("PASS")
else:
    print("FAIL")





