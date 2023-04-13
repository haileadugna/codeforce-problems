def gcd(num1, num2):
    while num2:
        num1 %= num2
        num1, num2 = num2, num1
    
    return num1

def find_factors(num):
    factors = []
    d = 1

    while d * d <= num:
        if num % d == 0:
            factors.append(d)
            factors.append(num // d)
            
        d += 1
    
    if num > 1:
        factors.append(num)
    
    return sorted(factors)

num1, num2 = map(int, input().split())
num_queries = int(input())
cur_gcd = gcd(num1, num2)
factors = find_factors(cur_gcd)

for query in range(num_queries):
    low, high = map(int, input().split())

    modified_gcd = -1
    for factor in factors:
        if low <= factor <= high:
            modified_gcd = factor


    print(modified_gcd)
