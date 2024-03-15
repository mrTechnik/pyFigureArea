"""
Импортируем все до этого описанные классы
"""
from area.area_classes.CustomFigure import CustomFigure
from area.area_classes.Triangle import Triangle
from area.area_classes.Circle import Circle


class Area:
    """
    Класс Area представляет собой класс для вычисления площади различных фигур.
    """
    # __slots__ = ()
    def __init__(self, *args):
        """
        Конструктор класса Area. Принимает аргументы и инициализирует объект.

        :param args: Аргументы, используемые для создания объекта фигуры.
        """
        self.args = args

        # Проверка на аргумент и тип для круга
        if len(args) == 1 and isinstance(args[0], int):
            self.figure = Circle(*args)
        # Проверка на аргумент и тип для кастомной фигуры
        elif len(args) == 2 and (callable(args[0]) and hasattr(args[1], "__iter__")):
            self.figure = CustomFigure(*args)
        # Проверка на аргумент и тип для треугольника
        elif len(args) == 3 and (isinstance(args[0], int) and
                                 isinstance(args[1], int) and
                                 isinstance(args[2], int)):
            self.figure = Triangle(*args)
        else:
            raise ValueError("Number of arguments ain't matchs or(and) has incorrect type")

    def calc_area(self):
        """
        Метод для вычисления площади фигуры.

        :return: Площадь фигуры и метка соответствующей фигуры.
        """
        return self.figure.calc_area()
