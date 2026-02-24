print("Welcome to the tip calculator!")
bill=float(input("What was the total bill?"))
tip=int(input("How much tip would you like to give? 10, 12, or 15?"))
tip_amount=(bill*tip)/100
split_among=int(input("How many people to split the bill?"))
print("Each person should pay: $" + str(round((bill+tip_amount)/split_among,2)) )