# Welcome phrase
user_inp = input("Hi! Do you want to calculate your payrate?\nY or N")
if user_inp == 'y': 
    work_hours = -1.0
    
    while work_hours < 0 :
        user_inp = input("Enter Hours worked per day: ")
        try:
            work_hours = float (user_inp)
        except:
            print("Please enter a positive number in digits.")
    
    pay_per_hour = -1.0
    while pay_per_hour < 0 :
        user_inp = input("Enter you Pay per hour: ")
        try:
            pay_per_hour = float (user_inp)
        except:
            print("Please enter a positive number in digits.")

    print("You earn ", work_hours*pay_per_hour, " buckaroonies every day! Nice")

else :
    print("Okay! Have a nice day!")


    

