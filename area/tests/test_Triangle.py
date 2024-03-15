import unittest
from area.area_classes.Triangle import Triangle


class TestTriangle(unittest.TestCase):
    def test_triangle_area(self):
        # Проверка вычисления площади для прямоугольного треугольника
        triangle1 = Triangle(3, 4, 5)
        self.assertEqual(triangle1.calc_area(), (6.0, "right_triangle"))

        # Проверка вычисления площади для обычного треугольника
        triangle2 = Triangle(3, 4, 6)
        self.assertAlmostEqual(triangle2.calc_area()[0], 5.33268225, places=7)

    def test_right_triangle_check(self):
        # Проверка определения прямоугольного треугольника
        triangle1 = Triangle(3, 4, 5)
        self.assertTrue(triangle1.is_right_triangle())

        # Проверка определения обычного треугольника
        triangle2 = Triangle(3, 4, 6)
        self.assertFalse(triangle2.is_right_triangle())

    def test_invalid_input(self):
        # Проверка обработки недопустимого ввода
        with self.assertRaises(TypeError):
            # Передаем строку вместо числа
            Triangle("a", 4, 5)


if __name__ == '__main__':
    unittest.main()
