def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка! Деление на ноль."
    return x / y

print("Добро пожаловать в калькулятор!")
print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")

while True:
    # Запрашиваем выбор операции
    choice = input("Введите номер операции (1/2/3/4) или 'q' для выхода: ")

    if choice == 'q':
        print("Выход из программы.")
        break

    if choice in ['1', '2', '3', '4']:
        # Запрашиваем два числа
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка! Введите числовое значение.")
            continue

        # Выполняем операцию в зависимости от выбора
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Неверный ввод. Пожалуйста, выберите операцию снова.")
