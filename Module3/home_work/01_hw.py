# Дан список имен.
# Выведите все имена в одну строку через запятую

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

i = 1
list_names = ""
while i <= len(names):
    if i == 1:
        list_names = names[i-1]
    else:
        list_names = list_names + ", " + names[i-1]
    i += 1
print(list_names)

# Пример вывода:
# Иван, Ирина, Вячеслав, Василий, Петр
