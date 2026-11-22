colors = ("червоний", "помаранчевий", "жовтий", "зелений", "синій", "фіолетовий")
print("Кортеж кольорів:", colors)
print("Кількість елементів:", len(colors))
print("Перший колір:", colors[0])
print("Третій колір:", colors[2])
print("Останній колір:", colors[-1])
print("Перші три кольори:", colors[:3])
print("Кольори з індексу 2 до 4:", colors[2:5])
print("Кожен другий колір:", colors[::2])
search = "зелений"
if search in colors:
    print("Колір", search, "є у кортежі")
else:
    print("Кольору", search, "немає у кортежі")
print("Усі кольори по черзі:")
for i, color in enumerate(colors, start=1):
    print(i, "-", color)
more_colors = ("білий", "чорний")
all_colors = colors + more_colors
print("Об'єднаний кортеж:", all_colors)
print("Кількість кольорів після об'єднання:", len(all_colors))
first, second, third = more_colors + ("сірий",)
print("Розпакування:", first, second, third)