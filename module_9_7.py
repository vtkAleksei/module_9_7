def is_prime (func):
    def wrapper(*args):
        sum_abc = func(*args)
        count_divisors = 0
        for i in range (1, sum_abc + 1):
            if sum_abc % i == 0:
                count_divisors += 1
        if count_divisors == 2:
            print('Простое')
        else:
            print ('Составное')
        return sum_abc
    return wrapper

@is_prime
def sum_three (a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)

result = sum_three(2, 2, 2)
print(result)
