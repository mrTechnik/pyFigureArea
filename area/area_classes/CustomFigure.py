from area.area_classes.Figure import Figure


class CustomFigure(Figure):
    """
    Класс CustomFigure представляет собой пользовательскую фигуру и
    предоставляет возможность вычисления её площади с помощью пользовательской функции.
    """
    __slots__ = ("func", "arg_list")

    def __init__(self, func, arg_list):
        """
        Конструктор класса CustomFigure. Принимает функцию и список аргументов и инициализирует объект.

        :param func: Функция, используемая для вычисления площади фигуры.
        :param arg_list: Список аргументов, передаваемых в функцию для вычисления площади.
        """
        if not callable(func) or not hasattr(arg_list, "__iter__"):
            raise TypeError("Invalid type for func or(and) arg_list arguments!!!")
        self.func = func
        self.arg_list = arg_list

    def calc_area(self):
        """
        Метод для вычисления площади пользовательской фигуры.

        :return: Площадь пользовательской фигуры и метка "custom_figure".
        """
        return self.func(*self.arg_list), "custom_figure"
