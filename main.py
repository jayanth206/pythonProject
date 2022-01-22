
num1 = input('Enter first number : ')
num2 = input('Enter second number : ')
print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")

sum = float(num1) + float(num2)
sub = float(num1) - float(num2)
mul = float(num1) * float(num2)
div = float(num1) / float(num2)
select = int(input("Select operations form 1, 2, 3, 4 :"))
if select == 1:
        print('the sum is ',    sum)
elif select == 2:
        print('the diff is',sub)
elif select == 3:
        print('the mul is',mul)
elif select == 4:
        print('the div is',div)

else:
        print("Invalid input")




