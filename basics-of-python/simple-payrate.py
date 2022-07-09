# Simple Payrate Calculator
print("")
user_inp = input("Hi! Here you can calculate your Payrate!\nHow many hours do you work each day?")
hrs_per_day = float(user_inp)
user_inp = input("How much are you paid each hour?")
pay_per_h = float(user_inp)

# Calculate the payrate
print("You are paid:", hrs_per_day*pay_per_h, "buckaroos")
