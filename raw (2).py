balance = 4773
annualInterestRate = 0.2
i = 1
initialBalance = balance
minimumPayment = 10
while i < 13:
            balance = balance - minimumPayment * (1.0 + annualInterestRate/12.0)
            #print('Month: ' + str(i))
            #print('MinimumPayment: ' + str(minimumPayment))
            #print('Balance: ' + str(balance))
            i += 1
if balance > 0 and i == 12:
                    balance = initialBalance
                    i = 1
                    minimumPayment += 10
                    #print('Inside if')
print('Lowest Payment: ' + str(minimumPayment))