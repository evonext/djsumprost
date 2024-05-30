import tkinter as tk             # Импортируем библиотеку tkinter для создания GUI
from tkinter import ttk          # Импортируем модуль ttk из tkinter для использования расширенных виджетов
from tkinter import messagebox   # Импортируем модуль messagebox для отображения сообщений

# Функция для проверки, является ли число простым
def is_prime(n):
    if n <= 1:                   # Числа меньше или равные 1 не являются простыми
        return False
    for i in range(2, int(n**0.5) + 1):  # Проверяем делители до квадратного корня из n
        if n % i == 0:           # Если есть делитель, то число не простое
            return False
    return True                  # Если делителей нет, число простое

# Функция для вычисления суммы простых чисел
def calculate_sum():
    try:
        n = int(entry_number.get())  # Получаем введенное число из поля ввода и преобразуем в целое
        sum_primes = 0            # Инициализируем сумму простых чисел

        if combobox.get() == "for":  # Если выбран цикл for
            for i in range(2, n + 1):  # Перебираем числа от 2 до n включительно
                if is_prime(i):    # Проверяем, является ли число простым
                    sum_primes += i  # Если да, добавляем его к сумме
        elif combobox.get() == "while":  # Если выбран цикл while
            i = 2
            while i <= n:          # Пока i не превысит n
                if is_prime(i):    # Проверяем, является ли число простым
                    sum_primes += i  # Если да, добавляем его к сумме
                i += 1
        label_result.config(text=f"Сумма простых чисел от 1 до {n}: {sum_primes}")  # Отображаем результат
    except ValueError:              # Обрабатываем ошибку, если введено не целое число
        messagebox.showerror("Ошибка ввода", "Пожалуйста, введите целое число")

# Функция для очистки полей
def clear_fields():
    combobox.set("")                # Очищаем выбор в combobox
    entry_number.delete(0, tk.END)  # Очищаем поле ввода числа
    label_result.config(text="Сумма простых чисел от 1 до :")  # Сбрасываем текст результата

# Создание главного окна
root = tk.Tk()                      # Создаем главное окно
root.title("Работа с виджетом Combobox")  # Устанавливаем заголовок окна

# Метка и выпадающий список для выбора типа цикла
label_cycle = tk.Label(root, text="Выберите цикл:")  # Создаем метку для выбора цикла
label_cycle.grid(row=0, column=0, padx=10, pady=5, sticky="e")  # Размещаем метку в сетке

combobox = ttk.Combobox(root, values=["for", "while"])  # Создаем выпадающий список для выбора цикла
combobox.grid(row=0, column=1, padx=10, pady=5, sticky="w")  # Размещаем выпадающий список в сетке

# Метка и поле ввода для числа
label_number = tk.Label(root, text="Введите целое число:")  # Создаем метку для ввода числа
label_number.grid(row=1, column=0, padx=10, pady=5, sticky="e")  # Размещаем метку в сетке

entry_number = tk.Entry(root)            # Создаем поле ввода для числа
entry_number.grid(row=1, column=1, padx=10, pady=5, sticky="w")  # Размещаем поле ввода в сетке

# Метка для отображения результата
label_result = tk.Label(root, text="Сумма простых чисел от 1 до :")  # Создаем метку для отображения результата
label_result.grid(row=2, column=0, columnspan=2, padx=10, pady=5)  # Размещаем метку в сетке

# Кнопка для выполнения вычислений
button_calculate = tk.Button(root, text="Выполнить", command=calculate_sum)  # Создаем кнопку для выполнения
button_calculate.grid(row=3, column=0, padx=10, pady=10, sticky="e")  # Размещаем кнопку в сетке

# Кнопка для очистки полей
button_clear = tk.Button(root, text="Очистить", command=clear_fields)  # Создаем кнопку для очистки
button_clear.grid(row=3, column=1, padx=10, pady=10, sticky="w")  # Размещаем кнопку в сетке

# Запуск основного цикла приложения
root.mainloop()                      # Запускаем главное окно

