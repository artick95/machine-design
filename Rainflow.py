import math
import cmath
import matplotlib.pyplot
import random
import turtle
import time

print ( 'is the data given in F(N) or sigma(MPa)?[1,2]' )
answer_dataType = int ( input () )

print ( 'insert k' )
k = float ( input () )

print ( 'insert B' )
B = float ( input () )

print ( 'inserire sigma_D-1' )
sigma_D_1 = float ( input () )

print('insert the number of peak+valleys')
number_peakValley=int(input())

sigma_D = [1]*number_peakValley
sigma_a_wave = [1]*number_peakValley
sigma_m_wave = [1]*number_peakValley
sigma_MAX = [1]*number_peakValley
sigma_MIN = [1]*number_peakValley
sigma_a = [1]*number_peakValley
sigma_m = [1]*number_peakValley
n = [1]*number_peakValley
alfa = [1]*number_peakValley
N = [1]*number_peakValley

i = 1

if answer_dataType == 1:  # F given
    F_max = [1]*number_peakValley
    F_min = [1]*number_peakValley
    F_m = [1]*number_peakValley
    F_a = [1]*number_peakValley

    print ( 'insert Area[mm^2]' )
    A = float ( input () )
    flag = 0
    while (flag != 1):
        print ( 'insert Fmin(i)[kN]' )
        F_min[i] = float ( input () )

        print ( 'insert Fmax(i)[kN]' )
        F_max[i] = float ( input () )

        print ( 'insert n(i)' )
        n[i] = float ( input () )

        F_a[i] = (F_max[i] - F_min[i]) / 2
        F_m[i] = (F_max[i] + F_min[i]) / 2


        # conversion
        sigma_a[i] = F_a[i] / A *1e3
        sigma_m[i] = F_m[i] / A*1e3
        sigma_MAX[i] = F_max[i] / A*1e3
        sigma_MIN[i] = F_min[i] / A*1e3

        N[i] = B / (sigma_a[i]**k)
        n_tot = math.fsum ( n )
        alfa[i] = n[i] / n_tot

        print ( 'Do you have more data?[1=continue,0=stop]' )
        answer_moreData = int ( input () )

        if answer_moreData == 1:
            i += 1
        if answer_moreData == 0:
            flag=1
            print ( "sigma_MAX[j] " + '\t' +  "sigma_MIN[j]" + '\t' + "sigma_m[j]" + '\t' + "sigma_a[j]" + '\t' +  "N[i]" + '\n' )
            for j in range ( 1, i  ):
                print (str(round(sigma_MAX[j],2)) + '\t' + str(round(sigma_MIN[j],2)) + '\t' + str(round(sigma_m[j],2)) + '\t' + str(round(sigma_a[j],2)) + '\t' + str(round(N[i],2)) + '\n' )
                j += 1

elif answer_dataType == 2:  # sigma given
    sigma_max = [1]*number_peakValley
    sigma_min = [1]*number_peakValley
    sigma_m = [1]*number_peakValley
    sigma_a = [1]*number_peakValley

    while (i < 200):
        print ( 'insert sigma_min(i)[N]' )
        sigma_min[i] = float ( input () )

        print ( 'insert sigma_max(i)[N]' )
        sigma_max[i] = float ( input () )

        print ( 'insert n(i) of min max current row' )
        n[i] = float ( input () )

        sigma_a[i] = (sigma_max[i] - sigma_min[i]) / 2
        sigma_m[i] = (sigma_max[i] + sigma_min[i]) / 2

        N[i] = B / (sigma_a ** k)

        print ( 'Do you have more data?[1=continue,0=stop]' )
        answer_moreData = str ( input () )
        if answer_moreData == 1:
            i += 1
        if answer_moreData == 0:
            for j in range ( 1, i + 1 ):
                print (
                    sigma_MAX[j] + '\t' + sigma_MIN[j] + '\t' + sigma_m[j] + '\t' + sigma_a[j] + '\t' + N[i] + '\n' )
                j += 1
            break


# print ( 'insert Rm so we can procede with statistical comparison analysis' )
# Rm = float ( input () )
#
# sigma_D[i] = sigma_D_1 - sigma_m[i] * sigma_D_1 / Rm
# sigma_a_wave[i] = sigma_a * sigma_D_1 / sigma_D
#
# N_wave = B / (sigma_a_wave[i] ** k)
#
# for j in range ( 1, i + 1 ) :
#     sigma_m_wave[j] = 0
#     print (
#         sigma_MAX[j] + '\t' + sigma_MIN[j] + '\t' + sigma_m_wave[j] + '\t' + sigma_a_wave[j] + '\t' + N_wave[
#             i] + '\n' )
#     j += 1
#
#
# N_tot_life = sum ( alfa / N_wave ) ** -1
# print ( 'N_tot_life= ' + str ( N_tot_life ) )
#
# print ( 'insert C' )
# C = float ( input () )
#
# sigma_cut_off = (C / 1e8) ** (1 / (2 * k - 1))
# print ( 'sigma_cut_off= ' + str ( sigma_cut_off ) )
#
# for j in range ( 1, i + 1 ) :
#     if sigma_a_wave > sigma_cut_off :
#         N_tot_failure = N_tot_life * n[j] / n_tot
#     else :
#         continue
#     j += 1
#
# print ( 'N_tot_life_failure= ' + str ( N_tot_failure ) )
