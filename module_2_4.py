# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# primes = []  # Создаем пустой список простых чисел
# not_primes = []  # Создаем пустой список не простых чисел
#
# def is_prime(n):  # Функция для проверки, является ли число простым
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# for num in numbers:
#     if num != 1:    # исключаем 1 из списка проверки
#         if is_prime(num):
#             primes.append(num)
#         else:
#             not_primes.append(num)
#
# print(primes)  # вывод на печать простые числа
# print(not_primes)  # вывод на печать не простые числа



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []                     # Создаем пустой список простых чисел
not_primes = []                 # Создаем пустой список не простых чисел

for num in range(len( numbers )):            # При помощи цикла for переберите список numbers.
    if num != 0 and  num != 1 :             # удаляем 0 и 1 из расчетов , т.к 1 не является ни простым, не непростым числом.
        is_prime = True             # Отметить простоту числа можно переменной is_prime, записав в неё занчение True перед проверкой.
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False    #   Если условие не выполняется, то False
                break               # прерывание цикла

        if is_prime:
            primes.append(num)       #   Добавляем простые числа в список primes
        else:
            not_primes.append(num)   #   Добавляем не простые числа в список not_primes

print(primes)                        # вывод на печать простые числа
print(not_primes)                    # вывод на печать не простые числа


