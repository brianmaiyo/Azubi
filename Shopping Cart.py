cart = [] #This initializes an empty list that will store the items added by the user.

while True: #infinite loop using while True:
            #The program continues running until the user chooses to exit.
    print("=== Shopping Cart ===")  #Just to make it cool
    #options for the customer
    print("1. Add item to cart")
    print("2. Remove item from cart")
    print("3. Display cart contents")
    print("4. Calculate total cost")
    print("5. Exit")
        #customers inputs the desired option. 
    option = input("Enter your option (1-5): ")
    
         #if else statements to prompt an action based on customers option
    if option == '1': # input is a string value hence the '1' in stead of 1.
        item_name = input("Enter the name of the item: ")
        item_price = float(input("Enter the price of the item: "))  #changing to price to float value (inputs are alwats of string type)
        item = {'name': item_name, 'price': item_price} #creates a dictionary called item
        cart.append(item) #adds the item dictionary into the cart list
        print("Item added to the cart.")   #feedback ot the customer that the item has been added

    elif option == '2':
        item_name = input("Enter the name of the item to remove: ")
        for item in cart:   #loops through the item dictionary in cart list
            if item['name'] == item_name: #cross checks for corresponding item name in the the item dictionary
                cart.remove(item) #removes the item
                print("Item removed from the cart.")    #feedback to customer
                break #terminates the loop when the item name matches the customers input
        else:
            print("Item not found in the cart.")

    elif option == '3':
        print("Items in the cart:")
        for item in cart:
            print(f"Name: {item['name']}, Price: {item['price']}")  #display the items plus price

    elif option == '4':
        total = sum(item['price'] for item in cart) #calculates sum of price for each item
        print(f"Total cost: {total}")

    elif option == '5':
        print("Thank you for using the shopping cart. Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")
