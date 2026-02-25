''' 
1) read currentmeterreading  and previousmeterreading

if units > 1000 then price : 1 unit = 10rs
if units >  800 and <= 1000 then price : 1 unit = 8rs
if units >  600 and <= 800 then price : 1 unit = 6rs
if units >  400 and <= 600 then price : 1 unit = 4rs
if units >  200 and <= 400 then price : 1 unit = 2rs
if units >  100 and <= 100 then price : 1 unit = 1rs
if units >  0 and <= 100 then price : 1 unit = 0.5rs
'''
# import sys

# Currmeter= int(sys.argv[1])
# Prevmeter = int(sys.argv[2])
# # Currmeter = int(input('enter the current meter: '))
# # Prevmeter = int(input('enter the previous meter: '))
# units = Currmeter - Prevmeter

# print(units)

# if units > 1000:
#     print(f"your current bil is : {units*10} ")
# elif units > 800:
#     print(f"your current bil is : {units*8} ")
# elif units > 600:
#     print(f"your current bil is : {units*6} ")
# elif units > 400:
#     print(f"your current bil is : {units*4} ")
# elif units > 200:
#     print(f"your current bil is : {units*2} ")
# elif units > 100:
#     print(f"your current bil is : {units*1} ")
# else:
#     print(f"your current bil is : {units*0.5} ")



'''
2) Acept the input as income > 5000rs per month else price will reduce by 50%
'''

# income = int(input('enter your monthly salary :'))

# if income > 5000:
#     print('You have to pay bill as shown:')
# else:
#     print('congratulations! you have got 50% discount ')


'''
greatest of 3 numbers a,b,c ---> which is greatest number
'''

# a = int(input('enter the first number:'))
# b = int(input('enter the second number:'))
# c = int(input('enter the third number:'))

# if a>b and a>c:
#     print('a is greatest!')
# elif b>a and b>c:
#     print('b is greater!')
# else:
#     print('c is greatest!') 


'''
4) CType : <E/N> CGenter : <M/F> PValue 

CType: E CGEn:M

Pvalue > 10000 --> 20% Discount, 1000Rs voucher
pvalue > 5000 and <=10000 15% discount 800Rs voucher
pvalue > 3000 and <=5000 10% discount 500Rs voucher
pvalue > 0 and <=3000 200rs Voucher

CType: E CGEn:F
pValue > 10000 --> 20% Discount, 800rs voucher
pvalue > 3000 and <= 10000 1540iscount, 400Rs voucher
pvalue > 3000 and <= 5000 10% discount, 200Rs Voucher
pvalue > 0 and <=3000 50rs Voucher
'''

CType = input('Please enter your customer Type E(existing) and N(New) Type (E/N):')
CGen = input('please enter your ender (M/F):')
Pvalue = int(input('enter the purchase value:'))

if CType.upper() == 'E':
    if CGen.upper() == 'M':
        if Pvalue >10000:
            print('congratulations! you have got 20% discount and 1000Rs voucher')
            print(f'Now you need to pay :RS{Pvalue-Pvalue*0.2}')
        elif Pvalue >5000:
            print('congratulations! you have got 15% discount and 800Rs voucher')
            print(f'Now you need to pay :RS{Pvalue-Pvalue*0.15}')
        elif Pvalue >3000:
            print('congratulations! you have got 10% discount and 500Rs voucher')
            print(f'Now you need to pay :RS{Pvalue-Pvalue*0.1}')
        else:
            print('congratulations! you have got 200Rs voucher')
            print(f'Now you need to pay :RS{Pvalue}')
    else:
        if Pvalue >10000:
            print('congratulations! you have got 20% discount and 800Rs voucher')
            print(f'Now you need to pay :RS{Pvalue-Pvalue*0.2}')
        elif Pvalue >5000:
            print('congratulations! you have got 15% discount and 400Rs voucher')
            print(f'Now you need to pay :RS{Pvalue-Pvalue*0.15}')
        elif Pvalue >3000:
            print('congratulations! you have got 10% discount and 200Rs voucher')
            print(f'Now you need to pay :RS{Pvalue-Pvalue*0.1}')
        else:
            print('congratulations! you have got 50Rs voucher')
            print(f'Now you need to pay :RS{Pvalue}')
else:
    if CGen.upper() == 'M' or 'F':
        print(f'Now you need to pay :RS{Pvalue}')

"================================================================"
"""=========================================================="""
