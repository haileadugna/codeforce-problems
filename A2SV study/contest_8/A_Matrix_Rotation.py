test_cases = int(input())

for _ in range(test_cases):

    num1, num2 = map(int, input().split())
    str1, str2 = map(int, input().split())
    res = "NO"
    if (num1 > num2 and str1 > str2) and (num1 < str1 and num2 < str2 ) : # and (num1 > str1 and num2 > str2 )
        res = "yes"
    
    elif num1 < num2 and str1 < str2 and (num1 > str1 and num2 > str2 ) : #and (num1 > str1 and num2 > str2 )
        res = "yes"

    elif (num1 > num2 and str1 > str2) and (num1 > str1 and num2 > str2 ) : # and (num1 > str1 and num2 > str2 )
        res = "yes"
    
    elif num1 < num2 and str1 < str2 and (num1 < str1 and num2 < str2 ) : #and (num1 > str1 and num2 > str2 )
        res = "yes"

    
    print(res)

    
