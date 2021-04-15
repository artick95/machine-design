import math


print('insert a[mm]')
a = float(input())


print('insert K_ic[MPa]')
K_ic = float(input())

print('insert desired SF')
SF = float(input())

print('is Y=sqrt(pi())?[1,0]')
answer_Y = float(input())

if answer_Y == 1:
    Y = math.sqrt(math.pi)
    print('ok we will assume Y as default :) \n')
else:
    print('please insert Y then... :)')
    Y = float(input())

sigma_lim = K_ic / (math.sqrt(a) * Y)
sigma_adm = K_ic / (math.sqrt(a) * Y * SF)

print('sigma_lim=' + str(sigma_lim) + ' MPa')
print('sigma_adm=' + str(sigma_adm) + ' MPa')
