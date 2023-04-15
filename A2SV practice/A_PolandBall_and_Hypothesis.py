num = int(input())


def is_prime(n):
    # If n is less than 2, it cannot be a prime number
    if n < 2:
        return False
    
    # Check if n is divisible by any number from 2 to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    # If n is not divisible by any number from 2 to the square root of n, it is a prime number
    return True

for j in range(1, 1000):
    temp = is_prime(j * num + 1)
    if not temp:
        print(j)
        break