import math

a = float(input("Enter the coefficient of x^2 (a): "))
b = float(input("Enter the coefficient of x (b): "))
c = float(input("Enter the constant term (c): "))

d = (b**2) - (4*a*c)

if d >= 0:
    
    sqrt_d = math.sqrt(d)
    sol1 = (-b - sqrt_d) / (2*a)
    sol2 = (-b + sqrt_d) / (2*a)
    print("The real roots are: {0} and {1}".format(sol1, sol2))
else:
    
    sqrt_d = math.sqrt(abs(d))
    real_part = -b / (2*a)
    imag_part = sqrt_d / (2*a)
    print("The complex roots are: {0} + {1}i and {0} - {1}i".format(real_part, imag_part))
