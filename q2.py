age=int(input("enter the age:"))
m_income= int(input("enter the monthly income:"))
existing_loan= float(int(input("enter the loan amount:")))
c_score =  float(input("enter the cibil score:"))


#loan_amount = income * 0.5
if age>=21 and age<=60 and m_income>25000  and c_score>700 and existing_loan<=m_income/2:
    print("eligible for loan")
else:
    print("not eligible for loan")