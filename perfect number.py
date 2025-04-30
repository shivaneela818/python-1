#c)Finding all the factors of a number and show whether it is a perfectnumber, i.e., the sumof all its factors (excluding the number itself)
#is equal to the numberitself.
n = int(input("Enter any number: "))
sum1 = 0

# Loop through all numbers less than 'n' to find divisors
for i in range(1, n):
    if n % i == 0:
        sum1 += i  # Add divisor to sum1

# Check if the sum of divisors equals the original number
if sum1 == n:
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")
