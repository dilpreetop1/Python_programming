marks= int(input("enter the marks:"))
per = marks/20*100
#print(per)
if per>=80 and marks>15:
    print("eligible for all streams")
elif per>70 and per<79 and marks>10 and marks==15:
    print("eleigble for science stream")
elif per>=60 and per <=69 and marks>5 and marks==10:
    print("eligible for humanities")
else:
    print("not eligible")