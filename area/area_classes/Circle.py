from area.area_classes.Figure import Figure


class Circle(Figure):
    """
    Класс Circle представляет собой подкласс (наследник) абстрактного класса Figure и представляет круг.
    """
    __slots__ = "r"

    def __init__(self, r):
        """
        Конструктор класса Circle. Принимает радиус круга и инициализирует объект.

        :param r: Радиус круга.
        """
        super().__init__()
        # Проверка типа
        if type(r) not in (int, float):
            raise TypeError("Type of r is not int or float")
        self.r = r

    def calc_area(self):
        """
        Метод для вычисления площади круга.

        :return: Площадь круга и метка "circle".
        """
        r = self.r
        return round(3.14 * r ** 2, 4), "circle"
