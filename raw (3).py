balance = 999999
annualInterestRate = 0.18
monthint = annualInterestRate / 12
montlow= 0.0
montupp=balance
payment=0.0

def Fixedbalance(balance, pay):
    for i in range(12):
        balance = (balance - pay) * (1 + monthint)
    return balance

def payment(startbalance):
    balance = startbalance
    montlow= balance/12
    montupp=(balance*(1+ monthint)**12)/12
    while  balance < -0.01 or balance > 0.01:
        pay = (montlow+montupp)/2
        balance = Fixedbalance(startbalance, pay)
        if balance < -0.01:
            montupp=pay
        elif balance > 0.01:
            montlow=pay
        else:
            return pay

print "Lowest Payment: " + str(round(payment(balance),2))