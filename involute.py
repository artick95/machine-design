import math
import cmath
import matplotlib.pyplot
import random
import turtle
import time

print('inserire alfa')
alfa=float(input())

print('inserire x1')
x1=float(input())

print('inserire x2')
x2=float(input())

print('inserire z1')
z1=float(input())

print('inserire z2')
z2=float(input())

other_side=math.tan(alfa*math.pi/180)-alfa*math.pi/180+2*(x1+x2)/(z1+z2)*math.tan(alfa*math.pi/180)

print('the number we need to converge to is = '+str(other_side))


alfa_w_try=21
while(alfa_w_try<89):
    diff=math.fabs(math.tan(alfa_w_try*math.pi/180)-alfa_w_try*math.pi/180-other_side)
    print(alfa_w_try)
    if (diff)<0.0001:
        alfa_working_final=alfa_w_try
        print('alfa-working is equal to '+ str(alfa_working_final))
        break
    else:
        print(diff)
    alfa_w_try+=0.00001