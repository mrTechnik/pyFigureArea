import unittest
from area.area_classes.CustomFigure import CustomFigure


class TestCustomFigure(unittest.TestCase):
    def test_custom_figure_area(self):
        # Проверка вычисления площади для пользовательской фигуры
        def custom_area_func(*args):
            return args[0] * args[1]  # Произведение первых двух аргументов

        custom_figure = CustomFigure(custom_area_func, [3, 4])
        self.assertEqual(custom_figure.calc_area(), (12, "custom_figure"))

    def test_invalid_input(self):
        # Проверка обработки недопустимого ввода
        with self.assertRaises(TypeError):
            # Передаем строку вместо функции
            CustomFigure("a", [4, 5])


if __name__ == '__main__':
    unittest.main()