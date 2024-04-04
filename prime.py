num = int(input("Enter a number to check if it's prime: "))

if num <= 1:
    prime = False
elif num <= 3:
    prime = True
elif num % 2 == 0 or num % 3 == 0:
    prime = False
else:
    prime = True
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            prime = False
            break
        i += 6

if prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
