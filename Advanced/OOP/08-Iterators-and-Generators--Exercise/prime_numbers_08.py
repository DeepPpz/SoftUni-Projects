def get_primes(numbers):
    is_prime = False
    
    for n in numbers:
        if n <= 1:
            continue
        
        if all(n % i != 0 for i in range(2, n)):
            is_prime = True
        
        if is_prime:
            is_prime = False
            yield n
