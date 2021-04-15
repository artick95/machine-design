import math
import cmath
import matplotlib.pyplot
import random
import turtle
import time

print ( 'sphere(1) or cylinder(2) or general(3)?[1,2,3]' )
answer_geometry = float ( input () )

print ( 'insert alfa_x[1/mm]' )
alfa_x = float ( input () )
print ( 'insert beta_x[1/mm]' )
beta_x = float ( input () )
print ( 'insert alfa_y[1/mm]' )
alfa_y = float ( input () )
print ( 'insert beta_y[1/mm]' )
beta_y = float ( input () )

d_wave = alfa_x + alfa_y + beta_x + beta_y
print('d_wave= '+str(d_wave)+' mm')

cos_tau = math.fabs ( alfa_x - alfa_y - (beta_x - beta_y) ) / d_wave
print ( 'cos_tau= ' + str ( cos_tau ) )

print ( 'insert Fc[N]\n(stribeck or contact)' )
Fc = float ( input () )
E = 2 * 10 ** 5  # MPa

print ( 'same material for both?[1,2]' )
answer_material = float ( input () )

if answer_material == 1:
    print ( 'insert v(Poisson)' )
    v = float ( input () )
    v1=v
    v2=v
    E1=E
    E2=E

elif answer_material == 2:
    print ( 'insert v1(Poisson)' )
    v1 = float ( input () )
    print ( 'insert v2(Poisson)' )
    v2 = float ( input () )
    print('insert E1[MPa]')
    E1 = float(input())
    print('insert E2[MPa]')
    E2 = float(input())

if answer_geometry == 1:
    #f = ((3 / 2 * Fc /(4*d_wave)) * ((1-v1**2)/E1+(1-v2**2)/E2)) ** (1 / 3)
    f = ((3 / 2 * Fc / (2 * d_wave)) * ((1 - v1 ** 2) / E1 + (1 - v2 ** 2) / E2)) ** (1 / 3)

    print ( 'f= ' + str ( f ) + ' mm' )

    print ( 'insert a_asterisk\n (a*=b* for perfect sphere to sphere, cos(tau)=0)' )
    a_asterisk = float ( input () )
    b_asterisk = float(input())

    a = a_asterisk * f
    b = b_asterisk * f

    print('a= '+str(a)+' mm')
    print('b= '+str(b)+' mm')

    p_max = 3 / 2 * Fc / (math.pi * a*b *f** 2)
    p_mean = p_max * 2 / 3
    # p_max=1.61*Reh
    print ( 'p_max= ' + str ( round(p_max,2) ) + 'MPa' )
    print ( 'p_mean= ' + str ( round(p_mean,2) ) + 'MPa' )
elif answer_geometry == 2:

    print ( 'insert L[mm]' )
    L = float ( input () )

    b =math.sqrt(4 * Fc / (2 * math.pi * L * (d_wave)) * ((1 - v1 ** 2) / E1 + (1 - v2 ** 2) / E2))
    print('b= '+str(b)+' mm')

    p_max = 2 * Fc / (math.pi * L * b)
    p_mean = p_max * math.pi / 4
    # p_max=1.67*Reh

    print ( 'p_max= ' + str ( round(p_max,2) ) + 'MPa' )
    print ( 'p_mean= ' + str ( round(p_mean,2) ) + 'MPa' )
elif answer_geometry == 3:
    f = ((3 / 2 * Fc / (2*d_wave)) * ((1-v1**2)/E1+(1-v2**2)/E2)) ** (1 / 3)
    print('f= '+str(f)+' mm')

    print ( 'insert a_asterisk' )
    a_asterisk = float ( input () )

    print ( 'insert b_asterisk' )
    b_asterisk = float ( input () )

    a = a_asterisk * f
    b = b_asterisk * f

    p_max = 3 / 2 * Fc / (math.pi * a * b)
    p_mean = p_max * 2 / 3
    # p_max=1.61*Reh
    print ( 'p_max= ' + str ( round(p_max,2) ) + 'MPa' )
    print ( 'p_mean= ' + str ( round(p_mean,2) ) + 'MPa' )
