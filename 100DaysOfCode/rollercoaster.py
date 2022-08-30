print("Welcom to the rollercoaster")
height = int(input("What is your height in cm? "))
age = int(input("How old are you? "))
bill = 0

if height >= 120:
    print("you can ride the rollercoaster!")
    if age <=12:
        bill = 5
        print("Please pay $5.")
    elif age <=18:
        bill = 7
        print("Please pay $7.")
    else:
        print("Please pay $12.")
        bill = 12

    pic = input("do you want a photo take? Y or No. ")
    if pic == "Y":
        bill += 3
    
    print(f"your finall bill is {bill}")
    
else:
    print("Sorry, you have to grow taller before you can ride.")