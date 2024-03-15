from abc import abstractmethod, ABC


class Figure(ABC):
    """
    Абстрактный класс Figure - базовый класс для геометрических фигур.
    У него есть два абстрактных метода: __init__ и calc_area.
    Класс Figure содержит слоты, для ограниченного набора атрибутов.
    """
    __slots__ = ()

    #  Абстрактный онструктор __init__ используется для инициализации объектов класса у потомков
    @abstractmethod
    def __init__(self):
        pass

    # Абстрактный метод calc_area предназначен для вычисления площади фигуры
    @abstractmethod
    def calc_area(self):
        pass
