import math



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

def Bisect(f, left, right, max, tol):
    print("This is Bisection Method")
    iter = 0
    
    while (abs(right - left) > tol and iter < max):
        iter += 1
        p = (left + right) / 2
        
        if ((f(left) < 0 and f(p) > 0) or (f(left) > 0 and f(p) < 0)):
            right = p
        else:
            left = p
    print(f"Root of {p} after {iter} iterations")

def FixedPoint(g, p0, tol, n0):
    i = 1
    
    print("This is Fixed-Point Method")
    
    while (i <= n0):
        p = g(p0)
        if math.isnan(p):
            print("Diverges")
            print("Failed after",i, "iterations")
            break
        
        print(i,": ",p)
        
        if (abs(p-p0) < tol):
            print("Converges")
            print("Successful after",i, "iterations")
            break
        i += 1
        p0 = p
    
def Newton(h, h_p, p_prev, tol, max):
    print("This is Newton's Method")
    
    i = 1
    
    while (i <= max):
        h_value = h(p_prev)
        h_p_value = h_p(p_prev)
        
        if (h_p_value != 0):
           p_next = (p_prev - h_value) / h_p_value 
           if (abs(p_next - p_prev) < tol):
               print(f"{p_next}")
               return p_next
               break
           i += 1
           p_prev = p_next
        else:
            print("The derivative is too small")
            break
    print("Max iterations reached")
    print(f"{p_prev}")
        
            
            
        
    
    
    
    
        
    
        
    
    