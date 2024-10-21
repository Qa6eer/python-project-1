units = float(input("Enter the number of electricity units consumed: "))

if units <= 50:
    total_bill = units * 0.50
elif units <= 150: 
    total_bill = (50 * 0.50) + ((units - 50) * 0.75)
elif units <= 250:
    total_bill = (50 * 0.50) + (100 * 0.75) + ((units - 150) * 1.20)
else:
    total_bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((units - 250) * 1.50)

surcharged_bill = 0.20 * total_bill

print("Total Electricity Bill in Rupees: ", surcharged_bill)
