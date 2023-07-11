
amount= float(input('Enter the charge for the food \n'))
result1= round(0.18*amount,2)
result2= round(0.07*amount,2)
print(f'Tip is = ${result1}')
print(f'Sales tax = ${result2}')
print(f'Grand total =${amount+result1+result2}')


