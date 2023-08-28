import math

# a*x**3 + b*x**2 + c*x + d = 0

def cubic_equation(a,b,c,d):

    # Δ = 18*a*b*c*d - 4*b**3*d + b**2*c**2 - 4*a*c**3 - 27*a**2*d**2
    Δ0 = b**2 - 3*a**3
    Δ1 = 2*b**3 - 9*a*b*c + 27*a**2*d

    u1 = 1
    u2 = complex(-1, math.sqrt(3)) * 0.5
    u3 = complex(-1, -math.sqrt(3)) * 0.5

    C = ((Δ1 + math.sqrt(Δ1**2 - 4*Δ0**3))/2)**(1/3)
    
    x1 = (-1/(3*a)) * (b + u1*C + Δ0/(u1*C))
    x2 = (-1/(3*a)) * (b + u2*C + Δ0/(u2*C))
    x3 = (-1/(3*a)) * (b + u3*C + Δ0/(u3*C))
    
    print (x1, x2, x3)

cubic_equation(1,-math.sqrt(3),-2,2*math.sqrt(3))