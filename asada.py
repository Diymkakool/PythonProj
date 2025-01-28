import math

def calculator():
    print("Добро пожаловать в расширенный калькулятор!")
    print("Вы можете выполнять следующие операции:")
    print("1. Арифметические операции (+, -, *, /)")
    print("2. Возведение в степень (x^y)")
    print("3. Вычисление квадратного корня (√x)")
    print("4. Модуль числа (|x|)")
    print("5. Факториал числа (n!)")
    print("6. Тригонометрические функции (sin, cos, tan)")
    print("Введите 'q' для выхода.")

    while True:
        operation = input("\nВведите номер операции (1/2/3/4/5/6) или 'q' для выхода: ")

        if operation == 'q':
            print("Выход из программы.")
            break

        try:
            if operation == '1':
                expression = input("Введите арифметическое выражение (например, 3 + 5 * 2): ")
                result = eval(expression)  # Вычисляем выражение
                print(f"Результат: {result}")

            elif operation == '2':
                base = float(input("Введите основание (x): "))
                exponent = float(input("Введите степень (y): "))
                print(f"{base}^{exponent} = {math.pow(base, exponent)}")

            elif operation == '3':
                number = float(input("Введите число для извлечения квадратного корня: "))
                if number < 0:
                    print("Ошибка! Квадратный корень не может быть отрицательным.")
                else:
                    print(f"√{number} = {math.sqrt(number)}")

            elif operation == '4':
                number = float(input("Введите число для вычисления модуля: "))
                print(f"|{number}| = {abs(number)}")

            elif operation == '5':
                number = int(input("Введите целое число для вычисления факториала: "))
                if number < 0:
                    print("Ошибка! Факториал определен только для неотрицательных чисел.")
                else:
                    print(f"{number}! = {math.factorial(number)}")

            elif operation == '6':
                angle = float(input("Введите угол в градусах: "))
                radians = math.radians(angle)  # Преобразуем градусы в радианы
                print(f"sin({angle}) = {math.sin(radians)}")
                print(f"cos({angle}) = {math.cos(radians)}")
                print(f"tan({angle}) = {math.tan(radians)}")

            else:
                print("Неверный выбор. Попробуйте снова.")

        except ValueError:
            print("Ошибка! Некорректный ввод. Попробуйте снова.")
        except ZeroDivisionError:
            print("Ошибка! Деление на ноль.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

calculator()
