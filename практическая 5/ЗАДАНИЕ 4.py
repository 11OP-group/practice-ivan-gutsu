import math
width = float(input("Введите ширину: "))
height = float(input("Введите высоту: "))

def calculate_rectangle_S(width, height):

    return width * height

def calculate_circle_S(radius):

    return math.pi * radius * radius

rectangle_S = calculate_rectangle_S(width, height)
print(f"Площадь прямоугольника: {rectangle_S:.2f}")

radius = float(input("Введите радиус: "))

circle_S = calculate_circle_S(radius)
print(f"Площадь круга: {circle_S:.2f}")