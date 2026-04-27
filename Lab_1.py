import random
from string import ascii_lowercase, ascii_uppercase

def custom_all(element):
    for item in element:
        if not isinstance(item, (int, float)):
            return False
    return True

def run_task_1():
    print("\nЗадача 1: Работа со списком")
    print("Введите элементы списка через пробел:")
    user_input = input("--> ")
    input_list = []
    for item in user_input.split():
        try:
            num = float(item)
            if num.is_integer():
                input_list.append(int(num))
            else:
                input_list.append(num)
        except ValueError:
            input_list.append(item)

    print(f"\nПолученный список: {input_list}")
    has_positive = any(isinstance(x, (int, float)) and x > 0 for x in input_list)
    print(f"1. Есть ли положительное число (any): {has_positive}")
    all_numbers = custom_all(input_list)
    print(f"2. Все элементы числа (all): {all_numbers}")
    try:
        sorted_list = sorted(input_list)
        print(f"3. Отсортированный список (sorted): {sorted_list}")
    except TypeError:
        print("3. Сортировка невозможна: список содержит смешанные типы.")

class CyclicTupleIterator:
    def __init__(self, data):
        self.data = tuple(data) if not isinstance(data, tuple) else data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.data:
            raise StopIteration
        value = self.data[self.index]
        self.index = (self.index + 1) % len(self.data)
        return value

def run_task_2():
    print("\nЗадача 2: CyclicTupleIterator")
    my_tuple = (10, 20, 30, 40)
    print(f"Исходный кортеж: {my_tuple}")
    cyclic_iter = CyclicTupleIterator(my_tuple)
    print("Вывод 8 элементов (циклично):")
    for i in range(8):
        print(f"  {next(cyclic_iter)}", end=" ")
    print()

def password_generator(n):
    chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
    while True:
        password = "".join(random.choice(chars) for _ in range(n))
        yield password

def run_task_3():
    print("\nЗадача 3: Генератор паролей (N=16)")
    n = 16
    gen = password_generator(n)
    print(f"Генерация 5 паролей длиной {n}:")
    for i in range(5):
        print(f"  Пароль {i+1}: {next(gen)}")

def run_task_4():
    print("\nЗадача 4: Числа Фибоначчи")

def main():
    while True:
        print("\n        МЕНЮ")
        print("1. Задача 1: Список (any, custom_all, sorted)")
        print("2. Задача 2: Циклический итератор для кортежа (CyclicTupleIterator)")
        print("3. Задача 3: Генератор паролей (N=16)")
        print("4. Задача 4: Числа Фибоначчи")
        print("0. Выход")

        choice = input("Выберите задачу (0-4): ")
        if choice == '1':
            run_task_1()
        elif choice == '2':
            run_task_2()
        elif choice == '3':
            run_task_3()
        elif choice == '4':
            run_task_4()
        elif choice == '0':
            print("Завершение работы программы.")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")
        if choice != '0':
            input("\nНажмите Enter, чтобы вернуться в меню...")

if __name__ == "__main__":
    main()
