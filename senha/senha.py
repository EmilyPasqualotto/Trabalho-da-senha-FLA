#sorteador de numeros------------------------------------#

from random import randint
a=(randint(0,9))
b=(randint(0,9))
c=(randint(0,9))
d=(randint(0,9))
e=(randint(0,9))

#jg = jogadas------trial = tentativas--------------------#
jg=0

#--------------------------------------------------------#
print('-------------------------------------------------')
print('-----------WELLCOME TO THE GUESS GAME------------')
print('-------------------------------------------------')
print('   you have 10 antteps for guess the password')
print('-------------------------------------------------')
print('this game was developed by: Emily Pasqualotto')
print(' ')

#--------------------------------------------------------#
while True:
    
    s1=(int(input('enter the first number here: ')))
    s2=(int(input('enter the second number here: ')))
    s3=(int(input('enter the third number here: ')))
    s4=(int(input('enter the fourth number here: ')))
    s5=(int(input('enter the fifth number here: ')))

#p = pontuação-------------------------------------------#
    jg+=1
    p=0
    trial=(10-jg)
    if (s1) == (a):
        aa=('+1')
        p+=1
    elif (s1) == ((b)or(c)or(d)or(e)):

        aa=('0')
    else:
        aa = ('-1') 
#primeira casa ^-^---------------------------------------#

    if (s2) == (b):
        bb=('+1')
        p+=1
    elif (s2) == ((c)or(d)or(e)or(a)):
        bb=('0')
    else:
        bb = ('-1')
#segunda casa ^-^----------------------------------------#

    if (s3) == (c):
        cc=('+1')
        p+=1
    elif (s3) == ((d)or(e)or(a)or(b)):
        cc=('0')
    else:
        cc = ('-1')
#terceira casa ^-^---------------------------------------#

    if (s4) == (d):
        dd=('+1')
        p+=1
    elif (s4) == ((e)or(a)or(b)or(c)):
        dd=('0')
    else:
        dd = ('-1')
        
#quarta casa ^-^-----------------------------------------#
    if (s5) == (e):

        ee=('+1')
        p+=1
    elif (s5) == ((a)or(b)or(c)or(d)):
        ee=('0')
    else:
        ee = ('-1')
        
#quinta casa ^-^-----------------------------------------#


#para parar o código-------------------------------------#
    if p == 5:
        print(aa,bb,cc,dd,ee)
        print('you win')
        break

    if jg<10:
        print (aa,bb,cc,dd,ee)
        print ('you still have',trial,'attempts')
        print (' ')

    if jg==10:
        print (aa,bb,cc,dd,ee)
        print('you loose')
        break
#-------------------------------------------------------#
 

    


        
