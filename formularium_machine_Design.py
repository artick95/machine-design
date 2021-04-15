stop = 1

while (stop != 0):
    print(
        'how can I help? \n [1]FKM \n [2]Fracture \n [3]Bolts \n [4]Gears \n [5]LCF\n [6]Bearings\n [7]Fun Facts\n [8]Q&A')

    formulaSheets = ['You fucked', 'FKM', 'Fracture', 'Bolts',
                     'Gears', 'LCF', 'Bearings', 'Fun Facts','Q&A']

    formulaSheet_chosen = int(input())

    print(formulaSheets[formulaSheet_chosen])

    if (formulaSheet_chosen == 1):
        print(
            ' **FKM&Fatigue**\n Fail-Safe:keep changing like human bones,accept failure and replace\n Safe-Life:Car Tier avoid failure\n Wft=Wfb*2\n Wfb=pi*d^3/32\n FKM: sigmad=sigmad-1-sigmad-1/(alfa*Rm)*sigmam\n Msigma=aM*e-3Rm,c+bM\n aM=0.355 bM=-0.1 Rm in MPa\n sigmab--> totally alternate\n sigmatc-->totally mean\n tau-->totally mean\n Ix=pi*d^4/64\n Ip=Ix*2\n ntot_failure = 1/sum(alfai/Ni) just count the failure cycles\n Heibach extension e6-e8\n Larson Miller\n P=(T+460)/(C+logtrapture)\n M.H\n P=(teta-teta0)/(logt-logt0)\n Bousinnessque \n du=(1-ni^2)/E*F/rb\n sigma increase benchmarks get closer and final rought area gets bigger XD\n sigmacr=pi^2*E/lambda^2\n lambda = l/rho\n rho^2*a=J\n Pcr=pi^2*E*J/l0^2  ')
        print('load more ?[1-y][0-n]')
        extra_FKM = int(input())
        if extra_FKM == 1:
            print(
                ' sigmatc=(0.7-0.8)sigmab\nKt=sigmaz,max/sigmanom: stress concentration factor\n sigma_a_eff=sigmabmax/(1-xsi*deltay)\n xsi=2/h\n Kf=Kt/(1+sci*deltay)=Kt/(n(sigma)*n(tau):fatigue knotch factor\n 1<Kf<Kt\n Kftc=Kttc/nsigma(r)\n  Kfb=Ktb/(nsigma(d)*nsigma(r))\n **Gaugh Pollard**\n (sigmaab/sigmabd-1)^2+(tauat/taud-1)^2<=1 \n tautd-1=sigmad-1/sqrt(3)\n **SF**\n Sffatigue=1.5-4(1.5suggested for 97.5%fkm)\n Sfbuckling=6-10\n Sfductile brittle=1.1-2.5\n ntot_life = ntot_fail*sum(nall_i)/sum(nfail_i)')

    if (formulaSheet_chosen == 2):
        print(
            ' **Rapid Fracture** \n SF= Kic/Ki\n Ki=Ysqrt(a)*sigma\n sigma=P/(W*B)\n B: depth\n W: Base\n **Yield Safety**\n SFy=Rpo2/sigma\n sigma =P/((w-2a)*B)\n **Dimensioning**\n B=Max(Byielding,Brapid_fracture)\n da/dN=C*(deltaKi)^n\n deltaKi=Ydeltasigmasqrt(a)\n sigma(r,teta)=Ki,ii,iii*f(teta)/sqrt(2pi*r))')

    if (formulaSheet_chosen == 3):
        print(
            ' **BOLTSz** \n min(muK_max,muG_min)\n Fm,max=.9Rp02As/sqrt(1+k^2)\n k=2/ds*(.16*x+.58*d2*muG)\n Amin=(3%4)Fa/Rp02 (USE 4! and Famax)\n M16-->dn=16mm\n n=deltapk/deltap=La/Lk\n Ma=Fm*(0.16p+0.58*muG+Dkm/2*muK)\n Wt=pi*d^3/16\n k=tau/sigma\n SF=sigma_lim/sigma_a\n sigma_lim=sigma_a**0.9\n Proof load: Fp = As*Sp\n Yield Strenght: F= As*Rp02\n delta_sk=lsk/Es*An: sull cuore del nut\n ls=dn*(0.5-->exagonal or 0.4-->socket cap\n deltaGM=deltaG+deltaM\n deltaG=lG/Es*Ad3\n deltaM=lm/Ex*An\n lm=dn*(0.33dn-->tapped thread or 0.4--> botted joint\n lG=0.5*dn\n ')
        print('load more ?[1-y][0-n]')
        extra_Bolts = int(input())
        if extra_Bolts == 1:
            print(
                ' Fsa=Fa*deltap/(deltas+deltap)\n Fpa=Fa*deltas/(deltas+deltap)\n deltaFs=deltai/(deltas+deltap)\n alfaA=Fm,max/Fm,min\n Coarse thread--> higher stripping strenght less accuracy required fas assembly and mass production\n finethread__> higher load capacity As higher higher accuracy required\n Mg=Fa*d2/2*tan(alfa+phigprime):moment on thread\n ')

    if (formulaSheet_chosen == 4):
        print(
            ' **GEARSz**\n i=w1/w2=r2/r1=rb2/rb1=z2/z1=M2out/M1in\n m=2r/z\n p=pi()*m\n epsilonalfa=AE/pb\n z>=2/sinalfa\n AC<T1C (condition for minimum teeths:)\n z>=2/sin(alfat)*cos(beta)\n vn=w1*0T1(orT2)\n vt=T1E*w1(p(curvature)*w) \n Almen: sigmaH*vg*Ah*mu \n DIN --> epsilon_alfa>1, knotch,x,m\n ISO epsilon_alfa>1\n Lewis-->epsilonalfa=1, only Ft no notch\n w2^2*p2a*p2e=w1p1a*p1e (p is the curvature T1 to point)\n zetaA=-zetaE\n invalfaw= inv alfa+2*(x1+x2)/(z1+z2)*tanalfa\n invalfa=tanalfa-alfa(alfa in radiants because tan spouts radiants)\n tanalfat = tan alfan/cosbeta\n tanbetab = tan beta*cosalfat')
        print('load more ?[1-y][0-n]')
        extra_Gears = int(input())
        if extra_Gears == 1:
            print(
                ' epsilon alfa = AE/(pb or pt*cosalfat)\n epsilonbeta = b*tanbetab/(pt*coslafatat)\nepsilon = epsilonalfa+epsilonbeta\n b>3%4*pt\n pn=pt*cosbeta\n mn=mt*cosbeta\n radd=r+mn\n **Bendinging Fatigue Verification**\n wft=w*Ke*Kv*Kfalfa*Kfbeta\n sigmaF=wft/mn*Yf*Yepsilon*Ybeta\n Sf= sigmafd/digmaf>)1.8\n w=Ft/b\n **Surface Fatigue Wear Verification**\n sigmah=sqrt(wft*(u+1/(u*d1))*Zh*Zh*Zepsilon)\n Sh=sigmahd/sigmah>=(z1>20-->1.25 orz1<=20-->1.4)\n **Hobbing** -->barbetta precisa\n **Shaping**-->sega\n rprime=r/cos^beta\n zeqvirt=z/cos^beta\n pn=pt/cosbeta\n tanalfan=tanalfat*cosbeta\n mn=mtcosbeta  ')
            print('do you need lewis?[1-y][0-n]')
            lewis = int(input())
            if lewis == 1:
                print(' I=b*t^3/12\n sigmazmax=6*Ft*l/(b*t^2)\n sigmazmax=6*Ft*zprime/(b*y?2)\n Yl=6*hl/m/(s/l)^2:lewis factor\n contact ration factor Zepsilon\n Khb: lonfitudina load distribution factor\n Fa=Fsinbetab\n Ft=Fcosbetabcosalfa\n Fr=Fcosbetabsinalfa ')
            print('do you need Din bending formulas?[1-y][0-n]')
            din = int(input())
            if din == 1:
                print(
                    '**DIN**\n wft=w*Ki*Kv*Kfa*Kfb\n w: specific nominal pitch-line force\n Ki:overload factor non uniformities of torque due to drivin or driven machine\n Kv: dynamic factor internal additional forces due to the errors introduced by manifacturing\n femanifacturing accuracy level\n ke teeth material\n Cv pitch line velocity\n cb epsilonbeta\n v pitchile velocity\n Kfa load distribution facotr admissible base pirch deviation for wheel material\n Kfb longitudian load distribution factor Kfb = 1 spur Kfb = 1.2 conival misalignment of teeth and shaft in torsion and bending')
                print('continue??[1-y][0-n]')
                contin = int(input())
                if contin == 1:
                    print('sigmamax=sqrt(Fn*(1/rho1*1/rho2)\n *DIN SURFACE*\n wht=w*Ki*Kv*Kha*Khb\n Kha: sur load distribution\n ')
    if (formulaSheet_chosen == 5):
        print(
            ' **LCF** \n Basquin-Coffin \n epsilon_a=sigma_f/E*(2Nf)^b+epsilon_f(2Nf)^c\n Moffin: \n epsilon_a=sigma_f/E*(1-sigma_m/sigma_f)*(2Nf)^b+epsilon_f*(1-sigma_m/sigma_f)^c/b*(2Nf)^c\n delta_epsilon = delta_epsilon_e +delta epsilon_p\n SF=epsilon_lim/epsilon_p\n N<1e3\n lambda(T)*(deltaepsilonp)^n*Nf=C1 \n lambda(T)/lambda(T0)=Nf(T0=/Nf(T)\n TMC=LCF@Teq-->TmTmax ')

    if (formulaSheet_chosen == 6):
        print(
            ' **BEARINGS** \n F=K(deltai+deltao)^n\n n=1.1-->ball bearing\n n=1.5-->cylinder bearing\n p=3-->ball bearing\n p=10/3-->cylinder bearing\n pmax=1.61ReH-->ball bearing\n pmax=1.67Reh-->cylinder bearing\n z/b=0.48-->ball bearing\n z/b=0.78-->cylinder bearingdeltatot=F^1/n*(1/Kin^1/n+1/Kout^1/n)\n min(gmin%gmax)\n k=ni/ni1\n ni: real viscosity\n ni1: required viscosity\n F0=0.5R/cosalfa+0.5A/sin(alfa)\n C0/P0>=S0\n P0=X0Fr0+Y0Fa0\n deltaphi=deltar*cosphi*cosalfa+deltaa*sinalfa\n deltaphi=deltarcosphi-g/2\n convex:circle from inside+\n concave: raceway -\n **Palmgreen Provavility**\n deltaphi= zita*a*di/2*z0*deltaphi\n S=Si*So\n S=e^-(J0+Ji)*R^r+L^e')
        print('load more ?[1-y][0-n]')
        extra_Bearings = int(input())
        if extra_Bearings == 1:
            print(
                ' **Load Cases**\n I-a-->deltaa=0 phimax=pi/2 like olimpic flag vertical \n I-b-->deltaa=deltar/tgalfa phimax=pi small circle and big circle touch at the top like a toung \n II--> deltaa>deltar/tanalafa phimax=pi small circle in big circle\n Pu:fatigue limit \n eta: contamination factor\n L=a1 askf*(C/P)^p\n L_hour=Le6/(60*n)\n **no axial ONLY RADIAL** \n g=0-->Fcontact=4.08*Fr/Z\n g=0.6deltar--> Fcontact=5*Fr/z\n deltaij+deltaoj=((Fij/Kinner)^1/n+((Fij+Fc)/Kouter)^1/n=dr*cosphi-.5g\n its like an inertia\n pmax=2000pref(sphere-plane)\n pmax=150pref(sphere-racewayuu)\n pmax=300pref(cylinder-plane)\n pmax=40pref(cylinder-raceway uu)\n Peq=sqrt(sum(alfai*Pi^p))')
        print(' load load contact cases ?[1-y][0-n]')
        extra_Bearings2 = int(input())
        if extra_Bearings2 == 1:
            print(
                ' **GEAR TEETH CONTACT**\n pmax=2*F/(pi*b*l)\n b:ellipse half width\n l=teeth depht\n b=(2*F/(pi*l)*(1-vi^2)/(E*dwavy))^1/2\n **General**\n f=(3/2*F*((1-ni1^2)/E1+(1-ni2^2)/E2)*1/(2*dwave))^1/3\n p=3/2F/(pi*a*b)*sqrt(1-x^2-a^2-y^2/b^2)\n pm=F/(pi*a*b)\n b<a\n **Sphere-Sphere**\n alfax=alfay\n betax=betay\n cost=0 a*=b*=1\n a=f\n f:general eq\n pmax=3/2*F/(pi*a^2)\n pm=3/2*pmax\n **Cylinder-Cylinder**\n alfax=betax=0\n cost=\ a*->inf b*->0\n p=2F/(pi*L*b)*sqrt(1-y^2/b^2) \n pm=pmax*pi/2\n ')

    if (formulaSheet_chosen == 7):
        print(
            ' **Fun Facts**\n What is the difference between mechanical engineers and civil engineers?Mechanical engineers build weapons. Civil engineers build targets.')
        print(
            'Who designed the human body?\nThree engineering students were gathered together discussing the possible designers of the human body.\nOne said, "It was a mechanical engineer. Just look at all the joints!"\nAnother said, "No, it was an electrical engineer. The nervous system has many thousands of electrical connections."\nThe last one said, "No, actually it had to have been a civil engineer. Who else would run a toxic waste pipeline through the recreational area?"')
    if (formulaSheet_chosen == 8):
        print('cuscinetti necessari a sostenere un albero verticale-->ma due cuscinetti a contatto obliquo\n stud no head no head friction\n head friction screw\n carico assiale che si raggiunge nelle viti serrando al 90%Rp02->Otteniamo una forza minore di tale valore (non uguale nè superiore come era scritto nelle altre scelte) per via dellincertezza di serraggio\n helical pitch radius è maggiore del base radius\n cuscinetto a 4 contatti (puo reggere carichi assiali in entrambe le direzioni)\n effetto dellaumento della defomrabilità del pezzo (aiuta la verifica sulla funzionalità del giunto)\n sezione da considerare nella verifica statica della vite (sezione minima tra sezione alleggerita o sezione di nocciolo....ma NON il diametro nominale\n **ex with %t and P**\n ni=%*rpm [assume a mission of 1 min]\n ntot=sum(ni)\n alfai=ni/ntot\n Peq=(alfai*Pi^n)^1/n \n L=(C/P)^p ')

    print('need something else?[1-yes][0-no]')
    stop = int(input())
    if (stop == 0):
        print('see you later ;)')
    else:
        print('thanks Master GoodLuck ;)')
