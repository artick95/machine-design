sigma_max = []
sigma_min = []
sigma_m = []
sigma_a = []

print ( 'insert Area[mm^2]' )
A = float ( input () )

while (i < 200):
    print ( 'insert sigma_min(i)[N]' )
    sigma_min[i] = float ( input () )

    print ( 'insert sigma_max(i)[N]' )
    sigma_max[i] = float( input () )

    print ( 'insert n(i) of min max current row' )
    n[i] = float( input () )

    sigma_a[i] = (sigma_max[i] - sigma_min[i]) / 2
    sigma_m[i] = (sigma_max[i] + sigma_min[i]) / 2
    i += 1

    N[i] = B / (sigma_a ** k)

    print ( 'Do you have more data?[1=continue,0=stop]' )
    answer_moreData = str ( input () )
    if answer_moreData == 0:
        break
