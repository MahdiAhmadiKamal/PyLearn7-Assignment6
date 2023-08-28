import math

# a*x**3 + b*x**2 + c*x + d = 0

def cubic_equation(a,b,c,d):

    A = b/a
    B = c/a
    C = d/a
    # x**3 + A*x**2 + B*x + C = 0

    p = B - A**2/3
    q = 2*A**3/27 - A*B/3 + C

    Δ = q**2/4 + p**3/27
    
    if Δ > 0:
        x = (-q/2 + math.sqrt(Δ))**(1/3) + (-q/2 - math.sqrt(Δ))**(1/3) - A/3
        print (x)
    if Δ == 0:
        x1 = -2*(q/2)**(1/3) - A/3
        x2 = x3 = (q/2)**(1/3) - A/3
        print (x1, x2)
    if Δ < 0:
        x1 = (2/math.sqrt(3))*(math.sqrt(-p))*math.sin(math.asin(3*math.sqrt(3)*q/(2*math.sqrt(-p)**3))/3) - A/3
        x2 = (-2/math.sqrt(3))*(math.sqrt(-p))*math.sin((math.pi/3)+math.asin(3*math.sqrt(3)*q/(2*math.sqrt(-p)**3))/3) - A/3
        x3 = (2/math.sqrt(3))*(math.sqrt(-p))*math.cos((math.pi/6)+math.asin(3*math.sqrt(3)*q/(2*math.sqrt(-p)**3))/3) - A/3
        print (x1, x2, x3)

cubic_equation(1,-math.sqrt(3),-2,2*math.sqrt(3))

# cubic_equation (1,2,3,4)