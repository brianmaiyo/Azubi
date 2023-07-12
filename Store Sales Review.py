
products=['Sankofa Foods','Jamestown Coffee','Bioko Chocolate',
          'Blue Skies Ice Cream','Fair Afric Chocolate',
          'Kawa Moka Coffee','Aphro Spirit','Mensado Bissap','Voltic']
prices=[30,25,40,20,20,35,45,50,35]
last_week=[2,3,5,8,4,4,6,2,9]

# calculating the total price average for all products
sum=0
for cost in prices:
    sum=sum+cost
    
    average=sum/len(prices)
print(f'The total price average for all products is ${average}')

#create new price list that reduces the old prices by $5
new_list_of_prices=[]
for old in prices:
    new_price=old-5
    new_list_of_prices.append(new_price)
print(new_list_of_prices)
print()

#calculate the total revenue generated from the products
total=0
for i in range(0,len(new_list_of_prices)):
    total = total + (new_list_of_prices[i]*last_week[i])
print(f'The total revenue generated from the products is ${total}')
print()


#calculate the average daily revenue generated  from the products
print(f'The average daily revenue generated  from the products is ${total/7}')

#based on new prices, which products are less than $30
less_than_30 = {}  # Dictionary to store products priced less than 30

for i in range(len(new_list_of_prices)):
    if new_list_of_prices[i] < 30:
        less_than_30[products[i]] = new_list_of_prices[i]

print("Products priced less than 30:")
for product, new_list_of_prices in less_than_30.items():
    print(product, "-", new_list_of_prices)

