print ("Welcome to the tip calculator!")
initial_total = float(input("What was the total bill? $"))
percent = int(input ("What percentage tip would you like to gove? 10, 12, or 15? "))
people = int(input ("How many people to split the bill? "))


total_per_person = round(initial_total/people * (percent/100 + 1), 2)


message =f"Each person should pay: ${total_per_person}"

print (message)