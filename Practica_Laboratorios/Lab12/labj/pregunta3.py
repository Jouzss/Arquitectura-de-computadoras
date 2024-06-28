import math

X = 1000000016000000063
# X = 10403

# Esta función fue obtenida de una página web: https://ellibrodepython.com/numeros-primos-python
def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

def par_num_primos(n):
    cant = 0
    
    for i in range(2, n):
        if ((es_primo(i)) and (cant == 0)):
            if((n%i) == 0):
                primo_1 = i
                cant = 1
        elif((es_primo(i)) and (cant == 1)):
            if((n%i) == 0):
                primo_2 = i
                return [primo_1, primo_2]

def find_prime_factors(n):
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0: 
            factors.append(i)
            n //= i
        if n == 1:
            break
    if n > 1:
        factors.append(n)
    return list(set(factors))
                    
if __name__ == '__main__':

    primos = []

    primos = par_num_primos(X)

    print(primos)