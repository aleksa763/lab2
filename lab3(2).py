a = int(input("Введите время в секундах"))
b = int(input("Введите время в минутах"))
b_seconds = b*60
max_time = a if a > b_seconds else b_seconds
print("Наибольшее время:", max_time, "секунд")
