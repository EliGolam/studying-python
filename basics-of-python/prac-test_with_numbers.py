# Verify user input function
def verify_user_input (input_value):
    try:
        assign = float(input_value)
        return True
    except:
        print("Please enter a number")
        return False
    



number_array = [9, 21, 99, 82, 123, 101, 34, 48, -12, 49, 2, 32, 12, 97, 5, -23, 38, 19, -17]
largest_number = None
smallest_number = None

# Find largest number
for number in number_array :
    if largest_number == None or number > largest_number : 
        largest_number = number

# Find smallest number
for number in number_array :
    if smallest_number == None or number < smallest_number :
        smallest_number = number

print("The largest number in the array is:", largest_number, "\n")
print("The smallest number in the array is:", smallest_number, "\n")

# Array length -- len (array) is the faster method of course
length = 0 
for elem in number_array :
    length += 1

print(length, "?=", len(number_array))

# Find average of numbers 
print("Find Average of Array") 
sum_numbers = 0

for number in number_array :
    sum_numbers += number

average = sum_numbers / len(number_array)
print("Average of the number array is: ", round(average, 2))

# Find a number in the Array
user_inp = None
success_found = False

while success_found == False :
    user_inp = input("Hi, what number are you looking for in the array?")

    if verify_user_input(user_inp) :
        number_found = float(user_inp)

        for number in number_array :
            if number_found == float(number) :
                print("We found the number: ", number_found)
                success_found = True
                break

        if success_found : 
            print("You did it!!")
        else :
            print("We couldn't find the number: ", number_found) 
            leave_inp = input("Do you wish to keep trying?")
            if leave_inp == 'n' or leave_inp == 'no' or leave_inp == 'N' or leave_inp == 'No' :
                print("oh really????")
                break
  

print("Done !!")
