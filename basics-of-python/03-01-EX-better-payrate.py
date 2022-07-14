# Welcome phrase
user_inp = input("Hi! Do you want to calculate your payrate?\nY or N\n")
if user_inp == 'y': 
    work_hours = -1.0
    
    while work_hours < 0 :
        user_inp = input("Please enter a positive number in digits.\nEnter Hours worked per day: ")
        try:
            work_hours = float (user_inp)
            if work_hours > 0 : print("Great !!\n\n")
        except:
            print("Please enter a number")
    
    pay_per_hour = -1.0
    while pay_per_hour < 0 :
        user_inp = input("Please enter a positive number in digits.\nEnter you Pay per hour: ")
        try:
            pay_per_hour = float (user_inp)
            if pay_per_hour > 0 : print("Great !!\n\n")
        except:
            print("Please enter a number")

    print("You earn ", work_hours*pay_per_hour, " buckaroonies every day! Nice")

else :
    print("Okay! Have a nice day!")


    

