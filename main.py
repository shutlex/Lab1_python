var1 = int(input("Введіть ціле число для змінної var1: "))
var2 = float(input("Введіть дробове число для змінної var2: "))
var3 = int(input("Введіть ціле число для змінної var3: "))
var4 = float(input("Введіть дробове число для змінної var4: "))

addition = var1 + var2 + var3 + var4

subtraction = var1 - var2 - var3 - var4

multiplication = var1 * var2 * var3 * var4

division1 = var1 / var2
division2 = var3 / var4

power1 = var1 ** var2
power2 = var3 ** var4

integer_division = var1 // var3

modulus = var1 % var3

results = [addition, subtraction, multiplication, division1, division2, power1, power2, integer_division, modulus]

count_elements = len(results)
print(f"Кількість елементів у списку: {count_elements}")

print("Парні елементи списку:")
for element in results:
    if isinstance(element, int) and element % 2 == 0:
        print(element)

results[1], results[4] = results[4], results[1]
print("Список після зміни:")
print(results)

name = input("Введіть ваше прізвище та ім’я: ")

print("Виконавець даної лабораторної роботи:")
print(name)
print("Висновки:")
print("1. Навчились працювати зі змінними та функцією input.")
print("2. Застосували основні арифметичні операції на змінних.")
print("3. Виконали маніпуляції з елементами списку.")
