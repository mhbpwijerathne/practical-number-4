
salary = float(input("Enter salary "))


if salary >= 100000:
    bonus_percentage = 15
elif salary >= 50000:
    bonus_percentage = 10
else:
    bonus_percentage = 5

bonus_amount = (salary * bonus_percentage) / 100
total_salary = salary + bonus_amount

print("Bonus Percentage: " + str(bonus_percentage) + "%")
print("Bonus Amount: " + str(bonus_amount))
print("Total Salary (with bonus): " + str(total_salary))
