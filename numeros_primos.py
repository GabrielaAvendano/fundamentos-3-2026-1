for num in range (2,31):
    es_primo = True
    
    for divisor in range(2,num):
        if num % divisor == 0:
            es_primo = False
            break
        
    if es_primo:
        print(f"{num} es primo.")
    else:
        print(f"{num} no es primo.")