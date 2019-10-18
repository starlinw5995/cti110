# CTI-110 
# P4HW2 - MealTipTax
# William Starling
# 10-17-2019
#
# Tax percent.
taxpercent =.06

# Give loop a varible.
loop = 'y'

while loop == 'y':

    # Charge for the food.
    chargeforfood = float(input("Enter the charge for food: $"))
    print()
           
    # Tip Percentage.
    tip = float(input("Amount of Tip Percentage (.16, .18, or .20): "))
    print()
        
    #Calculate tax amount.
    tax_amount = chargeforfood * taxpercent

    #Calculate tip amount.
    tip_amount = chargeforfood * tip

    #Calculate Meal, Tip and Tax together.
    Totalcost = tax_amount + tip_amount + chargeforfood

    if tip != .16 and tip != .18 and tip != .20:
        print('Error, please enter the tip percentage (.16,.18 or .20):')
        print()
    else:
        print('Original Food Charge $',format(chargeforfood,'.2f'))
        print()
        print('Tip Amount $',format(tip_amount,'.2f'))
        print()
        print('Tax Amount $',format(tax_amount,'.2f'))
        print()
        print('Total cost of meal $',format(Totalcost,'.2f'))
        print()
        # Run program again.
        loop = input('Would you like to enter another tip? (y/n): ')
        print()
    
# End program.
while loop == 'n':
    print(end='')




