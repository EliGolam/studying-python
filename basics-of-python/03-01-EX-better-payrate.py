# Welcome phrase
user_inp = input("Hi! Do you want to calculate your payrate?\nY or N\n")
if user_inp == 'y': 
    work_hours = -1.0
    # Calculating work hours per week from user input 
    while work_hours < 0 :
        user_inp = input("Please enter a positive number in digits.\nEnter Hours worked per day: ")
        try:
            work_hours = float (user_inp)
            if work_hours > 0 : 
                print("Great !!\n\n")
                if work_hours*7 > 40 :
                    work_hours_above_40 = work_hours*7 - 40
                    work_hours_under_40 = 40.0
                else :
                    work_hours_under_40 = work_hours*7
                    work_hours_above_40 = 0
            # print(work_hours_above_40)
            # print(work_hours_under_40)

        except:
            print("Please enter a number")
    
    # User Input Pay/hour
    pay_per_hour = -1.0
    while pay_per_hour < 0 :
        user_inp = input("Please enter a positive number in digits.\nEnter you Pay per hour: ")
        try:
            pay_per_hour = float (user_inp)
            if pay_per_hour > 0 : print("Great !!\n\n")
        except:
            print("Please enter a number")

    # Calculate pay per week keeping into consideration that hours above 40 are paid 1.5 times more
    pay_per_week = (work_hours_under_40*pay_per_hour) + (work_hours_above_40*pay_per_hour*1.5)
    print("You earn ", pay_per_week ," buckaroonies every week! Nice")

else :
    print("Okay! Have a nice day!")


    

