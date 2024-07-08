import tkinter as tk
from tkinter import messagebox  # добавления модуля для messagebox
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("1000x900")


# Обработчик для команд checkbox
def on_check_var():
    print("Значение checkbox:", check_var.get())
# Создание переменной для хранения состояния флажка
check_var = tk.BooleanVar()
# Создание виджета Checkbutton
check_var = tk.BooleanVar()
checkbutton = tk.Checkbutton(root, text="Check me!", font=("Helvetica", 16))
checkbutton.pack(pady=5)
# Настройка параметров Checkbutton
checkbutton.config(
    text="Checked!",    # установка нового текста для Checkbutton
    font=("Helvetica", 14),  # установка нового шрифта и его размера
    bg="yellow",        # установка фонового цвета Checkbutton
    fg="black",         # установка цвета текста Checkbutton
    width=15,           # установка ширины Checkbutton
    height=2,           # установка высоты Checkbutton
    indicatoron=False,  # отключение индикатора - False = нет индикатора, True = есть индикатор
    variable=check_var, # связывание с переменной check_var
    command=on_check_var # добавления команды
)

# Обработчик для команд radio
def on_radio_change():
    print("Выбранное значение:", radio_var.get())
# Создание переменной для хранения состояния радиокнопок
radio_var = tk.StringVar()
radio_var.set("Option 1")  # Устанавливаем начальное значение
# Создание виджетов Radiobutton
radio1 = tk.Radiobutton(root, text="Option 1", variable=radio_var, value="Option 1")
radio2 = tk.Radiobutton(root, text="Option 2", variable=radio_var, value="Option 2")
# Упаковка радиокнопок в окно
radio1.pack(pady=5)
radio2.pack(pady=5)
# Настройка параметров Radiobutton
radio1.config(
    text="Первый вариант",         # Установка нового текста для радиокнопки
    font=("Arial", 12),            # Установка нового шрифта и его размера
    bg="lightcoral",               # Установка фонового цвета радиокнопки
    fg="black",                    # Установка цвета текста радиокнопки
    width=20,                      # Установка ширины радиокнопки
    height=3,                      # Установка высоты радиокнопки
    indicatoron=True,              # Включение индикатора (True = есть индикатор, False = нет индикатора)
    selectcolor="lightgreen",      # Цвет фона при выборе радиокнопки (фон кружочка)
    activebackground="pink",       # Цвет фона при нажатии на радиокнопку
    activeforeground="red",        # Цвет текста при нажатии на радиокнопку
    command=on_radio_change         # добавления команды
)

# Настройка параметров для второй радиокнопки
radio2.config(
    text="Второй вариант",         # Установка нового текста для радиокнопки
    font=("Arial", 12),            # Установка нового шрифта и его размера
    bg="lightblue",                # Установка фонового цвета радиокнопки
    fg="black",                    # Установка цвета текста радиокнопки
    width=20,                      # Установка ширины радиокнопки
    height=3,                      # Установка высоты радиокнопки
    indicatoron=True,              # Включение индикатора (True = есть индикатор, False = нет индикатора)
    selectcolor="yellow",          # Цвет фона при выборе радиокнопки (фон кружочка)
    activebackground="lightgreen", # Цвет фона при нажатии на радиокнопку
    activeforeground="blue",       # Цвет текста при нажатии на радиокнопку
    command=on_radio_change        # добавления команды
)


# Создание виджета Text
text_widget = tk.Text(root, height=5, width=40)
# Вставка начального текста в виджет Text
text_widget.insert(tk.END, "This is a Text widget\nYou can type text here.")
# Упаковка виджета Text в окно
text_widget.pack()

# Настройка параметров виджета Text
text_widget.config(
    height=4,                  # Установка высоты виджета (в строках текста)
    width=40,                  # Установка ширины виджета (в символах)
    bg="lightyellow",          # Установка фонового цвета виджета
    fg="darkblue",             # Установка цвета текста в виджете
    font=("Helvetica", 12),    # Установка шрифта и его размера
    padx=10,                   # Установка внутреннего отступа по горизонтали
    pady=5,                   # Установка внутреннего отступа по вертикали
    selectbackground="lightblue",  # Цвет фона выделенного текста
    selectforeground="black",  # Цвет текста выделенного текста
    wrap=tk.WORD,              # Перенос слов по границам (tk.CHAR для переноса по символам, tk.WORD для переноса по словам)
    state=tk.NORMAL            # Состояние виджета (tk.DISABLED для отключения редактирования)
)


def on_select(event):
    # Получаем индекс выбранного элемента
    index = listbox.curselection()
    # Получаем текст выбранного элемента
    selected_item = listbox.get(index)
    # Выводим выбранный элемент в консоль (можно сохранить в переменную)
    print("Selected Item:", selected_item)

# Создание виджета Listbox
listbox = tk.Listbox(root)
listbox.insert(1, "Item 1")
listbox.insert(2, "Item 2")
listbox.insert(3, "Item 3")
listbox.pack(pady=5)

# Настройка параметров виджета Listbox
listbox.config(
    height=3,                     # Установка высоты виджета (в строках)
    width=30,                     # Установка ширины виджета (в символах)
    bg="lightcyan",               # Установка фонового цвета виджета
    fg="darkgreen",               # Установка цвета текста в виджете
    font=("Arial", 12),           # Установка шрифта и его размера
    selectbackground="lightgreen",# Цвет фона выделенного элемента
    selectforeground="black",     # Цвет текста выделенного элемента
    activestyle='dotbox',         # Стиль активного элемента ('none', 'underline', 'dotbox')
    highlightbackground="blue",   # Цвет границы виджета
    highlightcolor="red",         # Цвет границы виджета при фокусе
    justify=tk.CENTER             # Отцентроивает текст, также может быть tk.RIGHT и tk.LEFT
)

# Привязка обработчика событий к выбору элемента в Listbox
listbox.bind('<<ListboxSelect>>', on_select)





# Обработчик для команд меню
def menu_command():
    messagebox.showinfo("Menu", "Menu item clicked!")

# Создание виджета Menu и привязка его к основному окну
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Создание подменю File
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=menu_command)  # Пункт меню Open
file_menu.add_command(label="Save", command=menu_command)  # Пункт меню Save
file_menu.add_separator()  # Разделитель
file_menu.add_command(label="Exit", command=root.quit)  # Пункт меню Exit, command=root.quit - закрытие root
menu_bar.add_cascade(label="File", menu=file_menu)  # Добавление подменю File в главное меню

# Создание подменю Edit
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=menu_command)  # Пункт меню Cut
edit_menu.add_command(label="Copy", command=menu_command)  # Пункт меню Copy
edit_menu.add_command(label="Paste", command=menu_command)  # Пункт меню Paste
menu_bar.add_cascade(label="Edit", menu=edit_menu)  # Добавление подменю Edit в главное меню

# Создание подменю Help
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=menu_command)  # Пункт меню About
menu_bar.add_cascade(label="Help", menu=help_menu)  # Добавление подменю Help в главное меню

# Настройка параметров подменю File
file_menu.config(
    bg="blue",                   # Фоновый цвет подменю
    fg="white",                  # Цвет текста в подменю
    font=("Arial", 12),          # Шрифт и размер текста
    tearoff=False,               # Отключение возможности "оторвать" подменю
    activebackground="red",      # Цвет фона активного элемента
    activeforeground="green",    # Цвет текста активного элемента
    disabledforeground="yellow"  # Цвет текста отключенного элемента
)

# Настройка параметров подменю Edit
edit_menu.config(
    bg="lightgray",           # Фоновый цвет подменю
    fg="black",               # Цвет текста в подменю
    font=("Arial", 12),       # Шрифт и размер текста
    tearoff=False,            # Отключение возможности "оторвать" подменю
    activebackground="blue",  # Цвет фона активного элемента
    activeforeground="white", # Цвет текста активного элемента
    disabledforeground="gray" # Цвет текста отключенного элемента
)

# Настройка параметров подменю Help
help_menu.config(
    bg="lightgray",           # Фоновый цвет подменю
    fg="black",               # Цвет текста в подменю
    font=("Arial", 12),       # Шрифт и размер текста
    tearoff=False,            # Отключение возможности "оторвать" подменю
    activebackground="blue",  # Цвет фона активного элемента
    activeforeground="white", # Цвет текста активного элемента
    disabledforeground="gray" # Цвет текста отключенного элемента
)


# Создание виджета Frame
frame = tk.Frame(root)
frame.pack(pady=5, padx=10)  # Упаковка виджета с внешними отступами по оси X и Y
frame.config(
    bg="lightblue",          # Установка фонового цвета фрейма
    bd=5,                    # Установка ширины границы фрейма
    relief=tk.SUNKEN         # Установка стиля границы фрейма на "утопленный"
)

# Создание виджета LabelFrame внутри Frame
labelframe = tk.LabelFrame(frame, text="LabelFrame")
labelframe.pack(pady=5, padx=10, fill="both", expand="yes")  # Упаковка виджета с внешними отступами по оси X и Y
labelframe.config(
    bg="lightyellow",        # Установка фонового цвета LabelFrame
    fg="black",              # Установка цвета текста заголовка LabelFrame
    bd=5,                    # Установка ширины границы LabelFrame
    relief=tk.GROOVE,        # Установка стиля границы LabelFrame на "канавку"
    font=("Arial", 14)       # Установка шрифта и размера текста заголовка LabelFrame
)

# Создание виджета Label внутри LabelFrame
label = tk.Label(labelframe, text="Inside LabelFrame")
label.pack()  # Упаковка виджета без дополнительных отступов



# Canvas widget
canvas = tk.Canvas(root, width=300, height=200)
canvas.pack(pady=5)
canvas.config(
    bg="white",              # Фоновый цвет
    bd=5,                    # Ширина границы
    relief=tk.RIDGE,         # Стиль границы
    highlightthickness=2,    # Толщина выделения
    highlightbackground="black" # Цвет выделения
)
# Многоугольник (треугольник)
polygon = canvas.create_polygon(50, 150, 150, 50, 250, 150, fill="green", outline="black", width=2)

# Овал (круг) внутри прямоугольника
oval = canvas.create_oval(50, 200, 150, 300, fill="yellow", outline="black", width=2)

# Прямоугольник
rectangle = canvas.create_rectangle(200, 50, 350, 100, fill="purple", outline="black", width=2)

# Текст
text = canvas.create_text(100, 30, text="Hello, Canvas!", font=("Helvetica", 16), fill="orange")

# Путь к PNG изображению
image_path = "image_01.png"
# Открытие изображения и изменение размера
original_image = Image.open(image_path)
resized_image = original_image.resize((50, 50))
# Конвертация в формат, подходящий для Tkinter
image = ImageTk.PhotoImage(resized_image)
# Отображение изображения на Canvas
canvas.create_image(100, 100, anchor=tk.NW, image=image)



# Scale widget
scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
scale.pack(pady=5)
scale.config(
    bg="lightgray",          # Фоновый цвет
    fg="black",              # Цвет текста
    troughcolor="blue",      # Цвет канавки
    width=20,                # Ширина виджета
    length=300,              # Длина виджета
    sliderrelief=tk.RAISED,  # Стиль границы ползунка
    tickinterval=10,         # Интервал меток
    highlightthickness=3,    # Толщина выделения
    highlightbackground="red", # Цвет выделения
    highlightcolor="green",  # Цвет выделения при фокусе
    showvalue=True,          # Показать текущее значение
    resolution=1,            # Шаг изменения значения
    sliderlength=30,         # Длина ползунка
    state=tk.NORMAL,         # Состояние (NORMAL или DISABLED)
    command=lambda value: print("Значение:", value) # Команда при изменении значения
)



# Функция для обработки изменения значения в OptionMenu
def on_option_change(*args):
    print("Выбранное значение:", var.get())
# Создание переменной для хранения значения OptionMenu
var = tk.StringVar(root)
var.set("Option 1")  # Установка начального значения
# Привязка функции к изменению значения переменной
var.trace("w", on_option_change)
# Создание виджета OptionMenu
option_menu = tk.OptionMenu(root, var, "Option 1", "Option 2", "Option 3")
option_menu.pack(pady=5)
# Настройка виджета OptionMenu
option_menu.config(
    bg="white",               # Фоновый цвет
    fg="black",               # Цвет текста
    font=("Arial", 12),       # Шрифт и размер текста
    bd=2,                     # Ширина границы
    relief=tk.GROOVE,         # Стиль границы
    activebackground="blue",  # Фоновый цвет при наведении
    activeforeground="white", # Цвет текста при наведении
    highlightbackground="red",# Цвет границы при фокусе
    highlightcolor="green",   # Цвет текста при фокусе
    highlightthickness=1,     # Толщина границы при фокусе
    anchor=tk.CENTER          # Выравнивание текста по центру
)



# Функция для обработки изменения значения в Spinbox
def on_spinbox_change():
    print("Текущее значение:", spinbox_variable.get())
# Создание переменной для хранения значения Spinbox
spinbox_variable = tk.StringVar()
# Создание виджета Spinbox
spinbox = tk.Spinbox(root, from_=0, to=10, textvariable=spinbox_variable)
spinbox.pack(pady=5)
# Настройка виджета Spinbox
spinbox.config(
    bg="white",              # Фоновый цвет
    fg="black",              # Цвет текста
    bd=2,                    # Ширина границы
    relief=tk.RAISED,        # Стиль границы
    font=("Arial", 12),      # Шрифт и размер текста
    command=on_spinbox_change # Привязка функции к изменению значения Spinbox
)



root.mainloop()