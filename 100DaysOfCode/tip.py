#if the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12
from selectors import EVENT_READ


print("Welcome to tip calculator!")

bill = float(input("What is the total bill? $"))
tip = int(input("What percentage tip would you like to give? "))
split = int(input("How many people to split the bill? "))
bill_with_tipy = tip / 100 * bill + bill


print(bill_with_tipy)