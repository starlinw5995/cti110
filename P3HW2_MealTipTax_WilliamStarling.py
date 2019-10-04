# CTI-110 
# P3HW2 - MealTipTax
# William Starling
# 10-03-2019
#
# Tax percent.
taxpercent =.06
# Charge for the food.
chargeforfood = float(input("Enter the charge for food: $"))

# Tip Percentage.
tip = float(input("Amount of Tip: "))

#Calculate tip amount.
tip_amount = chargeforfood * tip

#Calculate tax amount.
tax_amount = chargeforfood * taxpercent

#Calculate Meal, Tip and Tax together.
Totalcost = tax_amount + tip_amount + chargeforfood
if tip != .16 and tip != .18 and tip != .20:
    print('Error')
else:
    print('Original Food Charge $',format(chargeforfood,'.2f'))
    print('Tip Amount $',format(tip_amount,'.2f'))
    print('Tax Amount $',format(tax_amount,'.2f'))
    print('Total cost of meal $',format(Totalcost,'.2f'))
