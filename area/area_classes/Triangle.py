from area.area_classes.Figure import Figure


class Triangle(Figure):
    """
    Класс Triangle представляет собой подкласс (наследник) абстрактного класса Figure и представляет треугольник.
    """
    __slots__ = ("a", "b", "c")

    def __init__(self, a, b, c):
        """
        Конструктор класса Triangle. Принимает длины сторон треугольника и инициализирует объект.

        :param a: Длина стороны a.
        :param b: Длина стороны b.
        :param c: Длина стороны c.
        """
        super().__init__()
        # Проверка типов
        if type(a) not in (int, float) or \
                type(b) not in (int, float) or \
                type(c) not in (int, float):
            raise TypeError("Type of a or(and) b or(and) c are not int or float")
        sides = [a, b, c]
        sides.sort()
        self.a = sides[0]
        self.b = sides[1]
        self.c = sides[2]

    def calc_area(self):
        """
        Метод для вычисления площади треугольника.

        :return: Площадь треугольника.
        """
        # Проверка на прямоугольность
        if self.is_right_triangle():
            return 0.5 * self.a * self.b, "right_triangle"
        else:
            p = (self.a + self.b + self.c) / 2
            return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5, "triangle"

    def is_right_triangle(self):
        """
        Метод для определения, является ли треугольник прямоугольным.

        :return: True, если треугольник прямоугольный, иначе False.
        """
        return self.a ** 2 + self.b ** 2 == self.c ** 2