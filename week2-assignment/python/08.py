prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

#Extract the middle five primes: Create a new list containing the five primes in the middle of the original list.
middle_five_primes = prime_numbers[2:7]
print("Middle five primes:", middle_five_primes)

#Get every second prime: Create a new list containing every second number from the original list, starting from the beginning.
second_prime = prime_numbers[::2]
print("Every second prime:", second_prime)

#Use negative indexing: Create a new list containing the last three primes of the list.
last_three_primes = prime_numbers[-3:]
print("Last three primes:", last_three_primes)

#Reverse the list: Create a new list that contains all the elements of the original list in reverse order.
reversed_primes = prime_numbers[::-1]
print("Reversed primes:", reversed_primes)

#Descending Order: Sort the list in descending order and store it in a new list.
descending_primes = sorted(prime_numbers, reverse=True)
print("Primes in descending order:", descending_primes)