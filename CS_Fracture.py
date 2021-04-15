import math
import cmath
import matplotlib.pyplot
import random
import turtle
import time


print('insert a[mm]')
a=float(input())

print('insert B[mm]')
B=float(input())

print('insert W[mm]')
W=float(input())

print('insert K_ic[MPa]')
K_ic=float(input())


print('insert P[N]')
P=float(input())

print('is Y=sqrt(pi())?[1,0]')
answer_Y=float(input())

if answer_Y==1:
    Y=math.sqrt(math.pi)
    print ( 'ok we will assume Y as default :)' )
else:
    print('please insert Y then... :)')
    Y=float(input())


CS=K_ic/(Y*math.sqrt(a*10**-3)*P/(W*B))

print('CS_RAPID-FRACTURE= '+str(round(CS,3)))

