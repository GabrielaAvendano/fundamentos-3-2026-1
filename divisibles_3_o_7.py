for num in range(1,51):
    divisible_3 = num % 3 == 0
    divisible_7 = num % 7 == 0
    
    if (divisible_3 or divisible_7) and not (divisible_3 and divisible_7):
        print(num)