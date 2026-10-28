
tasks = []


def add_task(title):
    if not title.strip():
        print("Название задачи не может быть пустым.")
        return

    tasks.append({"title": title, "done": False})
    print("Задача добавлена.")


def list_tasks():
    if not tasks:
        print("Список задач пуст.")
        return

    for number, task in enumerate(tasks, start=1):
        status = "Выполнена" if task["done"] else "Активна"
        print(f'{number}. {task["title"]} — {status}')



def complete_task():
    list_tasks()
    if not tasks:
        return

    try:
        number = int(input("Орындалған тапсырманың нөмірі: "))
        if 1 <= number <= len(tasks):
            tasks[number - 1]["done"] = True
            print("Тапсырма орындалды деп белгіленді.")
        else:
            print("Қате: мұндай нөмір жоқ.")
    except ValueError:
        print("Қате: бүтін сан енгізіңіз.")


def delete_task():
    list_tasks()
    if not tasks:
        return

    try:
        number = int(input("Жойылатын тапсырманың нөмірі: "))
        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print(f"'{removed['title']}' тапсырмасы жойылды.")
        else:
            print("Қате: мұндай нөмір жоқ.")
    except ValueError:
        print("Қате: бүтін сан енгізіңіз.")



def main():
    while True:
        print("\n--- To-Do Manager ---")
        print("1. Добавить задачу")
        print("2. Показать задачи")
        print("3. Завершить задачу")
        print("4. Удалить задачу")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            add_task(input("Название задачи: "))
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            list_tasks()
            try:
                complete_task(int(input("Номер задачи: ")))
            except ValueError:
                print("Введите целое число.")
        elif choice == "4":
            list_tasks()
            try:
                delete_task(int(input("Номер задачи: ")))
            except ValueError:
                print("Введите целое число.")
        elif choice == "0":
            break
        else:
            print("Неизвестная команда.")


if __name__ == "__main__":
    main()
