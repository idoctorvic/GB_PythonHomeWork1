# Задача 2
# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

n = int(input('Enter a three digit number: '))
digit = 0
result = 0
while n > 0:
    digit = n%10
    result += digit
    n //= 10
print(result)