import random

# Create a list of 100 random numbers from 0 to 1000
random_numbers = [random.randint(0, 1000) for _ in range(5)]

# Display the original list
print("Original List:", random_numbers)
#sort list from min to max(without using sort())
n = len(random_numbers)
for i in range(n - 1):
    for j in range(0, n - i - 1):
        if random_numbers[j] > random_numbers[j + 1]:
            random_numbers[j], random_numbers[j + 1] = random_numbers[j + 1], random_numbers[j]
avg_even=0
avg_odd=0
print("Sorted List:", random_numbers)
# Calculate average for even and odd numbers

even_numbers1 = [num for num in random_numbers if num % 2 == 0]
odd_numbers1 = [num for num in random_numbers if num % 2 != 0]

print('even_numbers1',even_numbers1)
print('odd_numbers1',odd_numbers1)

#calculate average for even and odd numbers
for r_n in random_numbers:
    if r_n%2==0:
        print('even number',r_n)
        avg_even=(avg_even+r_n)/2
    else:
        avg_odd=(avg_odd+r_n)/2
        print('odd number',r_n)

#print both average result in consol
print('average for even number',avg_even)
print('average for odd number',avg_odd)