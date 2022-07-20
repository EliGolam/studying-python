# Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, 
# count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except 
# and print an error message and skip to the next number.

number_array = []
user_inp = None
user_exit = False

print("Hello! This is a small practice program for Python.\n")

while user_exit is False : 
    user_inp = input("Please enter a number:  ")
    if user_inp == 'done' :
        user_exit = True
        break

    try : 
        number_array.append(float(user_inp))
        print("Thank you!\n")
    except :
        print("Invalid Input\n")
    
    print("Enter done if you don't wish to continue")


# SUM, COUNT
sum = 0
count = 0
for number in number_array :
    sum += number
    count += 1

print(sum, count)

average = sum / count
print(average)
