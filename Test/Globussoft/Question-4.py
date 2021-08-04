import math
a, b, s, m, n = [int(x) for x in input("Enter two value: ").split()]
angle = math.atan((b*n)/(a*m)) * 180 / math.pi
velocity = math.sqrt(b*n*b*n+a*m*a*m) / s
print(round(angle,2),round(velocity,2))