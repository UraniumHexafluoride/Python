totalPaid=0.0
monthlyInterestRate=annualInterestRate/12.0
for month in range(1,13):
    print('Month: '+str(month))
    minmonthlyPayment=balance*monthlyPaymentRate
    print('Minimum monthly payment: '+str(round(minmonthlyPayment,2)))
    balance=(balance-minmonthlyPayment)*(1+monthlyInterestRate)
    print('Remaining balance: '+str(round(balance,2)))
    totalPaid=totalPaid+minmonthlyPayment

print('Total paid: '+str(round(totalPaid,2)))
print('Remaining balance: '+str(round(balance,2)))