from area.Area import Area, Triangle
from area.area_classes.Figure import Figure


def main():
    """
    Примеры использования пакета
    :return:
    """
    # заранее объявим основные переменные сторон
    radius = 2

    side_a = 3
    side_b = 4
    side_c = 5
    side_c_1 = 6

    area_func = lambda a, b: a * b
    rect_sides = [6, 10]

    # основным объектом является класс Area и, взависимости,
    # от передаваемых параметров выполняется расчёт площади определённой фигуры

    # например, при передаче одного параметра, идёт вычисление площади круга
    circle = Area(radius)
    print(circle.calc_area())

    # при передаче двух параметров
    # первый: функция с формулой для вычисления плащади кастомной фигуры
    # второй: список необходимых значений сторон
    # в примере приведён вариант вычисления площади прямоугольника
    rectangle = Area(area_func, rect_sides)
    print(rectangle.calc_area())

    # следующий вариант это вычисление площади треугольника по сторонам
    # Есть два варианта: 1) когда треугольник прямоугольный 2) когда он любой другой
    # Внутри класса Triangle при расчёте площади это учитывается и меняется формула если треугольник прямоугольный
    right_triangle = Area(side_a, side_b, side_c)
    print(right_triangle.calc_area())

    triangle = Area(side_a, side_b, side_c_1)
    print(triangle.calc_area())
    # P.s. проверка на возможность создания треугольника не проводится

    # Также можно напрямую обратиться к класам для создания фигур и расчёта площади
    figure = Triangle(side_a + 2, side_b - 1, side_c + 1)
    print(figure.calc_area())

    # Для создания новой фигуры необходимо создать новый класс наследуя его
    # от абстрактного класса Figure, в папке area -> area_classes
    # пример создания находится ниже

    class Rectangle(Figure):
        """
        Класс Rectangle представляет собой подкласс (наследник) абстрактного класса Figure и представляет прямоугольник.
        """
        __slots__ = ("a", "b")

        def __init__(self, a, b):
            """
            Конструктор класса Rectangle. Принимает длины сторон и инициализирует объект.

            :param a: Длина одной стороны.
            :param b: Длина другой стороны.
            """
            super().__init__()
            # Проверка типа
            if type(a) not in (int, float) or type(b) not in (int, float):
                raise TypeError("Type of r is not int or float")
            self.a = a
            self.b = b

        def calc_area(self):
            """
            Метод для вычисления площади прямоугольника.

            :return: Площадь круга и метка "rectangle".
            """
            a = self.a
            b = self.b
            return a * b, "rectangle"

    # Пример работы нового класса
    rectangle = Rectangle(*rect_sides)
    print(rectangle.calc_area())

    # При необходимости можно добавить автоматическое определение фигуры в конструктор
    # класса Area, т.к. к сожалению в Python нет нормальной возможности перегрузить методы класса (как в Java)


if __name__ == '__main__':
    main()
