import math
import cmath
import matplotlib.pyplot
import random
import turtle
import time


print('insert a[mm]')
a=float(input())


print('insert W[mm]')
W=float(input())

print('insert K_ic[MPa]')
K_ic=float(input())

print('insert Reh[MPa]')
R_eh=float(input())


print('insert P[N]')
P=float(input())

print('insert desired CS')
CS=float(input())

print('is Y=sqrt(pi())?[1,0]')
answer_Y=float(input())

if answer_Y==1:
    Y=math.sqrt(math.pi)
    print ( 'ok we will assume Y as default :)' )
else:
    print('please insert Y then... :)')
    Y=float(input())


B_rapid=CS*Y*math.sqrt(a*10**-3)*P/(K_ic*W)
B_yield=CS*P/((W-2*a)*R_eh)

print('B_rapid_fracture= '+str(B_rapid)+'[mm]')
print('B_yield= '+str(round(B_yield,2))+'[mm]')

B_design= max(B_rapid,B_yield)
print('\n \n \n B_design='+str(round(B_design))+'[mm]  (max of the 2 above)')