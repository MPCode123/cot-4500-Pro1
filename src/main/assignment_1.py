# Approximation Method
def Approximate(x0, tol):
    iter = 0
    diff = x0
    x = x0
    
    print("This is Approximation Method")
    print(iter , ": " , x)
    
    while (diff >= tol):
        iter += 1
        y = x
        x = (x/2) + (1/x)
        print(iter, ":" , x)
        diff = abs(x-y)
        
    # print("Reached end of iterations")
    print("It will converge after %d iterations" %iter)


def f(x):
    return x*x*x + x*x + 2

def Bisect(left, right, max, tol):
    iter = 0
    
    while (abs(right - left) > tol and iter < max):
        iter += 1
        p = (left + right) / 2
        
        if ((f(left) < 0 and f(p) > 0) or (f(left) > 0 and f(p) < 0)):
            right = p
        else:
            left = p
            
    return p

#def FixedPoint(p0, tol, n0):
    #i = 1
    
    #while (i <= n0):
       # p = 
    
        
    
    