
# Ask the user to enter the basic salary
basic_salary = float(input("Enter basic salary: "))

# Calculate allowances and deductions
hra = 0.20 * basic_salary  # HRA is 20% of basic
da = 0.10 * basic_salary   # DA is 10% of basic
pf = 0.12 * basic_salary   # PF is 12% of basic

# Calculate gross and net salary
gross_salary = basic_salary + hra + da
net_salary = gross_salary - pf

# Show the results
print("HRA =", hra)
print("DA =", da)
print("PF =", pf)
print("Gross Salary =", gross_salary)
print("Net Salary =", net_salary)
