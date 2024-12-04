numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []  # Создаем пустой список простых чисел
not_primes = []  # Создаем пустой список не простых чисел

def is_prime(n):  # Функция для проверки, является ли число простым
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for num in numbers:
    if num != 1:
        if is_prime(num):
            primes.append(num)
        else:
            not_primes.append(num)

print(primes)  # вывод на печать простые числа
print(not_primes)  # вывод на печать не простые числа
