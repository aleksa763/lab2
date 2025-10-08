n = int(input("Введите сумму n: "))
bills = [64, 32, 16, 8, 4, 2, 1]
result = []
for bill in bills:
    while n >= bill:
        n -= bill
        result.append(bill)
print("Список купюр для суммы:", result)
print("Минимальное количество купюр:", len(result))
