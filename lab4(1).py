names = input("Введите имена студентов через пробел: ").split()
i = 0
found = False
while i < len(names):
    name = names[i].lower()
    if name[0] == name[-1]:
        found = True
        break
    i += 1
if found:
    print("ДА")
else:
    print("НЕТ")
