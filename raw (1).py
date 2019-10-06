def evaluatePoly(poly2, x):
    sol=0.0
    for a in range(len(poly2)):
        sol+=poly2[a]*x**a
    return sol

def computeDeriv(poly1):
        dpoly=range(len(poly1))
        for aa in range(len(poly1)):
            dpoly[aa]=aa*poly1[aa]
        if len(poly1)==1:
            dpoly=[0.0,0.0]
        return dpoly[1:]

def computeRoot(poly, x_0, epsilon):
    '''
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a list containing the root and the number of iterations required
    to get to the root.
 
    poly: list of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: list [float, int]
    '''
    # FILL IN YOUR CODE HERE...
    
    iteracion=0
    derivada=computeDeriv(poly)
    if abs(evaluatePoly(poly,x_0))<=epsilon:
        x_1=x_0
        iteracion=0
    else:
        x_1=epsilon
    error=abs(x_1-x_0)
    while (error>epsilon):
        x_1=x_0 - (evaluatePoly(poly,x_0) / evaluatePoly(derivada,x_0))
        error=abs(x_1-x_0)
        iteracion+=1
        x_0=x_1
    return [x_1,iteracion]

## nao
print computeRoot([-13.39, 0.0, 17.5, 3.0, 1.0], 0.1,  .0001)
print [0.806790753796352, 7]
print computeRoot([1, 9, 8], -3, .01)
print [-1.0000079170005467, 5]
print computeRoot([1, -1, 1, -1], 2, .001)
print [1.0002210630197605, 4]