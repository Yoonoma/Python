from tkinter import *
from tkinter import ttk

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.patches import Rectangle, Circle
from random import randint
from math import pi
import matplotlib.pyplot as plt

'''
Выполнили студенты:
Батаев Я. А.

Преподаватель:
Гусятинер Л. Б.
'''

'''
Метод Монте-Карло
На плоскости нарисован квадрат заданного размера с левой нижней 
вершиной в начале координат. В квадрат вписывается окружность.
Случайным образом в квадрате выбирается 1000 точек. 

а) нужно определить, сколько точек попало внутрь круга
б) считая количество точек пропорциональным площади, найти отношение площадей
круга и квадрата
в) по этому отношению определить приближённое значение числа пи
г) определить, насколько найденное значение отличается от "библиотечного".
'''

fig, ax = plt.subplots()
ax.set_title('Моделирование')

# Работа с tkinter
root = Tk()
root.title("Метод Монте-Карло")

note = ttk.Notebook(root)
root.geometry("640x550")
ms = ttk.Frame(note)
note.add(ms, text="Main-Screen")

md = ttk.Frame(note)
note.add(md, text='Model')

note.pack()

colors = ["#444C5C", "#78A5A3", "red"]

A = 10000  # Сторона квадрата
R = A / 2  # Радиус окружности
total_points = 0  # Количество точек в окружности
count_throws = 1000  # Количество бросков

x_square = 0
y_square = 0

x_circle = R
y_circle = R

square = Rectangle((0, 0), A, A, facecolor='#444C5C', label='Квадрат')  # Объект квадрат
circle = Circle((R, R), R, color='#78A5A3', label='Окружность')  # Объект окружность

for _ in range(count_throws):
    x_points = randint(0, A)
    y_points = randint(0, A)
    plt.plot(x_points, y_points, 'ro')

    if (x_points - x_circle) ** 2 + (y_points - y_circle) ** 2 <= R ** 2:
        total_points += 1

f_attitude = total_points / count_throws  # Отношение площадей круга и квадрата по точкам
f_pi = (4 * total_points) / count_throws  # Pi методом Монте-Карло

ax.add_patch(square)
ax.add_patch(circle)

# Легенда
texts = ["Квадрат", "Окружность", "Точки"]
markers = ["s", "o", "."]

patches = [plt.plot([], [], marker=markers[i], markeredgewidth=1.8, ms=10, ls="", mec=None, color=colors[i],
                    label="{:s}".format(texts[i]))[0] for i in range(len(texts))]

plt.legend(handles=patches,
           bbox_to_anchor=(1.01, 1.01),
           loc='upper right',
           facecolor='lightgray')
plt.grid()  # Сетка

# Отображение модели
canvas = FigureCanvasTkAgg(fig, master=md)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, md)
toolbar.update()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

# Main-screen

text_line = Label(ms, font="Arial 13", justify='left', text=f'Количество точек в окружности : {total_points}\n' \
                                                            f'Отношение площадей круга и квадрата по точкам ' \
                                                            f'= {f_attitude}\nПриблизительное значение числа ' \
                                                            f'Пи = {f_pi}\nРазница найденного числа Пи от "библиотечного " = {pi - f_pi}').place(
    x=30, y=150)

root.mainloop()
