cost_price = int(input("Enter the cost price: "))
selling_price = int(input("Enter the selling price: "))

profit = selling_price - cost_price
loss = cost_price - selling_price

if selling_price > cost_price:
    print("You made a profit of:", profit)
elif selling_price < cost_price:
    print("You incurred a loss of:", loss)
elif selling_price == cost_price:
    print("No profit, no loss.")
