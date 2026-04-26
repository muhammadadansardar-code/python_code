#normal sciling
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Index 2 se 5 tak (lekin 5 shamil nahi hoga)
print(my_list[2:5])    # Output: [2, 3, 4]

# Shuru se index 4 tak
print(my_list[:4])     # Output: [0, 1, 2, 3]

# Index 5 se bilkul akhir tak
print(my_list[5:])     # Output: [5, 6, 7, 8, 9]


#negative slicing 
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Akhri 3 elements nikalna
print(my_list[-3:])    # Output: [7, 8, 9]

# -5 se lekar -2 tak (lekin -2 shamil nahi)
print(my_list[-5:-2])  # Output: [5, 6, 7]