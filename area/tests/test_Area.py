import unittest
from area.Area import Area


class TestArea(unittest.TestCase):
    def test_circle_area(self):
        # Проверка вычисления площади круга
        area = Area(5)
        self.assertEqual(area.calc_area(), (78.5, "circle"))

    def test_custom_figure_area(self):
        # Проверка вычисления площади пользовательской фигуры
        area = Area(lambda x: x ** 2, [5])
        self.assertEqual(area.calc_area(), (25, "custom_figure"))

    def test_triangle_area(self):
        # Проверка вычисления площади треугольника
        area = Area(3, 4, 5)
        self.assertEqual(area.calc_area(), (6.0, "right_triangle"))

    def test_invalid_input(self):
        # Проверка обработки недопустимого ввода
        with self.assertRaises(ValueError):
            # Передаем строку вместо числа
            Area("3", 4, 5)


if __name__ == '__main__':
    unittest.main()