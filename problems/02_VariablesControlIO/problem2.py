currentAmount = float(input('How much is in your bank account?'))
interestRates = float(input('What is the monthly interest rate?'))
monthsToSave = int(input('How many months do you plan saving?'))


for month in range(monthsToSave):
	currentAmount = currentAmount + (currentAmount * interestRates)
	print('Month {} - {}'.format(month, currentAmount))

print('Total amount of money after interest is: ' + str(currentAmount))