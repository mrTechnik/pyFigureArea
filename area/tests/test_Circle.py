import unittest
from area.area_classes.Circle import Circle


class TestCircle(unittest.TestCase):
    def test_circle_area(self):
        # Проверка вычисления площади круга
        circle = Circle(5)
        self.assertEqual(circle.calc_area(), (78.5, "circle"))

    def test_invalid_input(self):
        # Проверка обработки недопустимого ввода
        with self.assertRaises(TypeError):
            # Передаем строку вместо числа
            Circle("1")


if __name__ == '__main__':
    unittest.main()