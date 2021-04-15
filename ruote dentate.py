import math


# print('insert radius of wheel 1[mm]')
# r1=float(input())
#
# print('insert radius of wheel 2[mm]')
# r2=float(input())

print ( 'insert modulus' )
m = float ( input ( ) )

print ( 'insert z1' )
z1 = float ( input ( ) )

print ( 'insert z2' )
z2 = float ( input ( ) )

print ( 'insert alfa[deg]' )
alfa = float ( input ( ) )

i = z2 / z1

print ( 'i= ' + str ( round ( z2 / z1 , 2 ) ) )

r1 = m * z1 / 2
r2 = m * z2 / 2
print ( 'r1= ' + str ( round ( r1 , 2 ) ) + ' mm' )
print ( 'r2= ' + str ( round ( r2 , 2 ) ) + ' mm' )

r1_add = r1 + m
r2_add = r2 + m
print ( 'r1_add= ' + str ( round ( r1_add , 2 ) ) + ' mm' )
print ( 'r2_add= ' + str ( round ( r2_add , 2 ) ) + ' mm' )

rb1 = r1 * math.cos ( alfa * math.pi / 180 )
rb2 = r2 * math.cos ( alfa * math.pi / 180 )
print ( 'rb1= ' + str ( round ( rb1 , 2 ) ) + ' mm' )
print ( 'rb2= ' + str ( round ( rb2 , 2 ) ) + ' mm' )

pb=2*math.pi*rb1/z1
p=2*math.pi*r1/z1

print ( 'pb= ' + str ( round ( pb , 2 ) ) + ' mm' )
print ( 'p= ' + str ( round ( pb , 2 ) ) + ' mm' )


CT2 = r2 * math.sin ( alfa * math.pi / 180 )
CT1 = r1 * math.sin ( alfa * math.pi / 180 )
print ( 'CT1= ' + str ( round ( CT1 , 2 ) ) + ' mm' )
print ( 'CT2= ' + str ( round ( CT2 , 2 ) ) + ' mm' )

AT2 = math.sqrt ( r2_add ** 2 - rb2 ** 2 )
AC = AT2 - CT2

ET1 = math.sqrt ( r1_add ** 2 - rb1 ** 2 )
CE = ET1 - CT1

AE = CE + AC

ET2 = CT2 - CE
AT1 = CT1 - AC

print ( 'ET1= ' + str ( round ( ET1 , 2 ) ) + ' mm' )
print ( 'AT1= ' + str ( round ( AT1 , 2 ) ) + ' mm' )
print ( 'ET2= ' + str ( round ( ET2 , 2 ) ) + ' mm' )
print ( 'T2A= ' + str ( round ( AT2 , 2 ) ) + ' mm' )

print ( 'AC= ' + str ( round ( AC , 2 ) ) + ' mm' )
print ( 'CE= ' + str ( round ( CE , 2 ) ) + ' mm' )

print ( 'AE= ' + str ( round ( AE , 2 ) ) + ' mm' )
print ( 'pb= ' + str ( round ( pb , 2 ) ) + ' mm' )
print('epsilon_alfa= '+str(round(AE/pb,2))+' [-]')

print ( 'a= ' + str ( round ( r1 + r2 , 2 ) ) )


rE=math.sqrt(rb2**2+ET2**2)
delta_r=r2_add-rE
h=2.25*m
percentage_contactHeight=delta_r/h

print('rE= '+str(round(rE,2))+'mm')
print('delta_r= '+str(round(delta_r,2))+'mm')
print('h= ' + str(round(h, 2)) + 'mm')
print('percentage_contactHeight= '+str(round(percentage_contactHeight,2))+'mm')


KE=AE-pb
HK=pb-KE

print('AH= '+str(round(KE,2))+'mm (zone to the sides with half the load)')
print('HK= '+str(round(HK,2))+'mm (zone to the center with the load)')


print ( 'do you want to proceed with speed calculations?[1,0]' )
answer_speed = float ( input ( ) )

if answer_speed == 1 :
    print ( 'insert w1' )
    w1 = float ( input ( ) )
    w2 = w1 / i

    v1n_A = rb1 * w1
    v1t_A = AT1 * w1
    v1_A = math.sqrt ( v1n_A ** 2 + v1t_A ** 2 )

    print ( 'v1n_A= ' + str ( round ( v1n_A , 2 ) ) + ' mm/s' )
    print ( 'v1t_A= ' + str ( round ( v1t_A , 2 ) ) + ' mm/s' )
    print ( '|v1_A|= ' + str ( round ( v1_A , 2 ) ) + ' mm/s' )

    v2n_A = rb2 * w2
    v2t_A = AT2 * w2
    v2_A = math.sqrt ( v2n_A ** 2 + v2t_A ** 2 )
    vg_A = v1t_A - v2t_A
    print ( 'vg_E= ' + str ( round ( vg_A , 2 ) ) + ' mm/s' )
    print ( 'v2n_A= ' + str ( round  ( v2n_A , 2 ) ) + ' mm/s' )
    print ( 'v2t_A= ' + str ( round ( v2t_A , 2 ) ) + ' mm/s' )
    print ( '|v2_A|= ' + str ( round ( v2_A , 2 ) ) + ' mm/s' )

    v1n_C = rb1 * w1
    v1t_C = CT1 * w1
    v1_C = math.sqrt ( v1n_C ** 2 + v1t_C ** 2 )

    print ( 'v1n_C= ' + str ( round ( v1n_C , 2 ) ) + ' mm/s' )
    print ( 'v1t_C= ' + str ( round ( v1t_C , 2 ) ) + ' mm/s' )
    print ( '|v1_C|= ' + str ( round ( v1_C , 2 ) ) + ' mm/s' )

    v2n_C = rb2 * w2
    v2t_C = CT2 * w2
    v2_C = math.sqrt ( v2n_C ** 2 + v2t_C ** 2 )
    vg_C = v1t_C - v2t_C
    print ( 'vg_C= ' + str ( round ( vg_C , 2 ) ) + ' mm/s' )
    print ( 'v2n_C= ' + str ( round ( v2n_C , 2 ) ) + ' mm/s' )
    print ( 'v2t_C= ' + str ( round ( v2t_C , 2 ) ) + ' mm/s' )
    print ( '|v2_C|= ' + str ( round ( v2_C , 2 ) ) + ' mm/s' )

    v1n_E = rb1 * w1
    v1t_E = ET1 * w1
    v1_E = math.sqrt ( v1n_E ** 2 + v1t_E ** 2 )

    print ( 'v1n_E= ' + str ( round ( v1n_E , 2 ) ) + ' mm/s' )
    print ( 'v1t_E= ' + str ( round ( v1t_E , 2 ) ) + ' mm/s' )
    print ( '|v1_E|= ' + str ( round ( v1_E , 2 ) ) + ' mm/s' )

    v2n_E = rb2 * w2
    v2t_E = ET2 * w2
    v2_E = math.sqrt ( v2n_E ** 2 + v2t_E ** 2 )
    vg_E = v1t_E - v2t_E
    print ( 'vg_E= ' + str ( round ( vg_E , 2 ) ) + ' mm/s' )
    print ( 'v2n_E= ' + str ( round ( v2n_E , 2 ) ) + ' mm/s' )
    print ( 'v2t_E= ' + str ( round ( v2t_E , 2 ) ) + ' mm/s' )
    print ( '|v2_E|= ' + str ( round ( v2_E , 2 ) ) + ' mm/s' )

    zita1A = vg_A / v1t_A
    zita2A = vg_A / v2t_A

    print('zita1A= ' + str(round(zita1A, 2)))
    print('zita2A= ' + str(round(zita2A, 2)))

    zita1C = vg_C / v1t_C
    zita2C = vg_C / v2t_C

    print('zita1C= ' + str(round(zita1C, 2)))
    print('zita2C= ' + str(round(zita2C, 2)))

    zita1E = vg_E / v1t_E
    zita2E = vg_E / v2t_E

    print('zita1E= ' + str(round(zita1E, 2)))
    print('zita2E= ' + str(round(zita2E, 2)))

    print ( '\n the end :)' )


elif answer_speed == 0 :
    print ( 'the end :)' )
