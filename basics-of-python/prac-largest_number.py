number_array = [9, 21, 99, 82, 123, 101, 34, 48, -12, 49, 2, 32, 12, 97, 5, -23, 38, 19, -17]
largest_number = None
smallest_number = None

for number in number_array :
    if largest_number == None or number > largest_number : 
        largest_number = number

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

print("Done !!")
