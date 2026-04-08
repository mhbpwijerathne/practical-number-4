
income = float(input("Enter income"))
if income >= 100000 :
    tax_percentage = 20
    
elif income >= 50000:
    tax_percentage = 10
    
else :
    tax_percentage = 0

tax_amount = (income * tax_percentage) / 100
final_income = income - tax_amount

print("tax_percentage: " + str(tax_percentage) + "%")
print("tax_amount: " + str(tax_amount))
print("final_income: " + str(final_income))


