# CTI-110
# P4HW1 - Expenses
# William Starling
# 10/17/2019
#
# This program calculates the users expenses.

# Initialize a counter for the number of expenses entered.
number_of_expenses = 1

# Make a variable to control loop.
expenses = 'y'

# Enter the starting amount in your account.
account = float(input('Enter starting amount in account? '))
print()

#Make a variable for the total of the expenses.
total_expenses = 0

# Begin the loop.
while expenses == 'y':

    # Get the expenses.
    expenses = float(input('Enter expense ' + str(number_of_expenses) + ' : '))

    #Calculate the total of expenses.
    total_expenses = total_expenses + expenses

    # Add 1 to the expense line everytime.
    number_of_expenses = number_of_expenses + 1

    # Ask if you want another expense.
    expenses = input('Do you want to enter another expense? (y/n) ')
    print()

# Display amount in account to begin with.    
if expenses == 'n':
    print('Amount in account before expense subtraction $',
          format(account,'.0f'))

    # Display number of expenses used.
    print('Number of expenses entered:', number_of_expenses - 1 ,'')
    print()

    #Calculate and display amount left in account.
    print('Amount in account AFTER expenses subtracted is $',
          format(account - total_expenses,'.0f'))

