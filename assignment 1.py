#Computer Application In Civil Engineering (CE 257)
"""
BOATENG CHRISTIAN
6932821

GitHub link: https://github.com/droxybellinton/Boateng-Christian.git
"""
import numpy as np
L = 12 #length of beam in meters(m)
w = 10 #intensity of load in KN/m
"""
SOLUTIONS
"""
#Question A

#Bending moment and shear force at the first end, x=0
x = 0
M = (w*(-6*x**2 + 6*L*x-L**2))/12
V = w*(L/2 - x)
m= 'The bending moment at x=0 is '
n= 'the shear force at x=0 is '
print()
print('(a.1)' + m + str(M) + ' and ', n + str(V))
#Bending moment(M) and shear force(V) at the first end, x=L=10
x = L
M = (w*(-6*x**2 + 6*L*x-L**2))/12
V = w*(L/2 - x)
a= 'The bending moment at x=L is '
b= 'the shear force at x=L is '
print()
print('(a.2)' + m + str(M) +' and ', n + str(V))

#Question B
""" 
When the bending moment is zero, we get an expression x**2 - Lx + L**2/6 = 0
"""
#from the expression 
a = 1
b = -L
c = L**2/6
#Using the Quadratic formula the two roots are;
discriminant = b**2 - 4*a*c
root_1b = (-b + np.sqrt(discriminant))/2*a
root_2b = (-b - np.sqrt(discriminant))/2*a
print()
print('(b) The points of contra-flexure are {0} and {1}'.format(root_1b,root_2b))

#Question C
""" 
Shear force is zero when x = L/2
"""
x = L/2
print()
print('(c) The point at which V=0 is {}'.format(x))

#Question D
p = 0
s = 0.01
q = L + s
x = np.arange(p,q,s) 
M = (w*(-6*x**2 + 6*L*x-L**2))/12
print()
print('(d) Using the initialized variable,the bending moment at each step in the array is {0}'.format(M))

#Question E
V = w*(L/2 - x)
print()
print('(e) The shear force for each step along the span is {}'.format(V))

#Question F
"""
Let the absolute value of the bending moment array be AV
Also let the minimum AV be m_AV
"""
AV =  abs(M)
m_AV = min(AV)
""" 
When the bending moment is m_AV, we get an expression x**2 - Lx + (L**2/6)+(2*m_AV)/w = 0
"""
#from the above expression 
a = 1
b = -L
c = (L**2/6)+(2*m_AV)/w
#Using the Quadratic formula the two roots are;
discriminant = b**2 - 4*a*c
root_1f = (-b + np.sqrt(discriminant))/2*a
root_2f = (-b - np.sqrt(discriminant))/2*a
print()
print('(f) The points along L at which the absolute values of the bending moment array is minimum are {0} and {1}'.format(root_1f,root_2f))

#Question G
"""
Let the relative errors be r_e
"""
r_e1 = ((root_1b - root_1f)/root_1b*100) 
r_e2 = ((root_2f - root_2b)/root_2f*100)
print()
print('(g) The relative errors between estimated points of contra-flexure are {0}% and {1}%'.format(r_e1,r_e2))

#Question H
"""
Let the maximum bending moment be max_BM and the minimum bending moment be min_BM
"""
#for the maximum
max_BM = max(M)
""" 
When the bending moment is max_BM, we get an expression x**2 - Lx + (L**2/6)+(2*max_BM)/w = 0
"""
a = 1
b = -L
c = (L**2/6)+(2*max_BM)/w
#Using the Quadratic formula the two roots are;
discriminant = b**2 - 4*a*c
root_1 = (-b + np.sqrt(discriminant))/2*a
root_2 = (-b - np.sqrt(discriminant))/2*a
print()
print('(h.1) The points at which the maximum bending moment occur are {0} and {1}'.format(root_1,root_2))

#for the minimum
min_BM = min(M)
""" 
When the bending moment is min_BM, we get an expression x**2 - Lx + (L**2//6)+(2*min_BM)/w = 0
"""
a = 1
b = -L
c = (L**2//6)+(2*min_BM)/w
#Using the Quadratic formula the two roots are;
discriminant = b**2 - 4*a*c
root_1 = (-b - np.sqrt(discriminant))/2*a
root_2 = (-b + np.sqrt(discriminant))/2*a
print()
print('(h.2) The points at which the minimum bending moment occur are {0} and {1}'.format(root_1,root_2))