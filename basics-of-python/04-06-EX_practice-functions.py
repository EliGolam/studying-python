def computepay (hours, rate) :
    hours_above_40 = 0
    hours_under_40 = 0

    if hours*7 > 40 :
        hours_above_40 = hours*7 - 40
        hours_under_40 = 40.0
    else :
        hours_under_40 = hours*7

    pay_rate = (hours_under_40*rate) + (hours_above_40*rate*1.5)
    return pay_rate

def verify_user_input (assign, input_value) :
    try:
        assign = float (input_value)
    except :
        print("Please enter a number\n")
        return -1.0
    if assign > 0 :
            print("Great !!\n\n")
            return assign
    else :
        print("Please enter a positive number")
        return -1.0     
        

# Welcome phrase
user_inp = input("Hi! Do you want to calculate your payrate?\nY or N\n")
if user_inp == 'y': 
    work_hours = -1.0
    # Calculating work hours per week from user input 
    while work_hours < 0 :
        user_inp = input("Please enter a positive number in digits.\nEnter Hours worked per day: ")
        work_hours = verify_user_input(work_hours, user_inp)
    
    # User Input Pay/hour
    pay_per_hour = -1.0
    while pay_per_hour < 0 :
        user_inp = input("Please enter a positive number in digits.\nEnter you Pay per hour: ")
        pay_per_hour = verify_user_input(pay_per_hour, user_inp)

    # Print Wage    
    print("You earn ", computepay(work_hours, pay_per_hour) ," buckaroonies every week! Nice")

else :
    print("Okay! Have a nice day!")


    

