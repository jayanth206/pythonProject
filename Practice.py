a = int(input('Weight : '))
kg = a/2.2046
lbs = a/1
print('type k or K if u want to convert to kg else type l or L ')
select = input('(K)g or (L)bs :')

if select == 'k' or 'K':
    print('weight in kg : ', kg)
elif select == 'l' or 'L':
    print(lbs)
else:
    print('none')
