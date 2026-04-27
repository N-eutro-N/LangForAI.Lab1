# пустое меню с заглушками функций

def run_task_1():
    print("\nЗадача 1: Работа со списком")

def run_task_2():
    print("\nЗадача 2: Циклический итератор")

def run_task_3():
    print("\nЗадача 3: Генератор паролей")

def run_task_4():
    print("\nЗадача 4: Числа Фибоначчи")

def main():
    while True:
        print("\n        МЕНЮ")
        print("1. Задача 1: Список (any, custom_all, sorted)")
        print("2. Задача 2: Циклический итератор")
        print("3. Задача 3: Генератор паролей")
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
