
import unittest
import os
from Christmas_tree import file

class TestsChristmasTree(unittest.TestCase):

    def setUp(self):                     # Удаляем файл "yolka.txt", если он существует, чтобы начать тестирование с "0"
        if os.path.exists("yolka.txt"):
            os.remove("yolka.txt")

    def test_creation(self):             # Тест на создание файла с ёлкой
        levels = 3
        file(levels)
        self.assertTrue(os.path.exists("yolka.txt"), "Должен быть создан файл yolka.txt")

    def test_content(self):              # Тест на содержимое файла для ёлки с уровнем 5
        levels = 5
        file(levels)
        with open("yolka.txt", "r") as f:
            content = f.read()

        expected_content = (
        "\n"
        "                 W\n"
        "                 *\n"
        "            @* * * * *\n"
        "         * * * * * * * * *@\n"
        "   @ * * * * * * * * * * * * *\n"
        " * * * * * * * * * * * * * * * * *@\n"
        "               TTTTT\n"
        "               TTTTT\n"
        )
        self.assertEqual(content, expected_content, "Содержимое файла не соответствует ожидаемому")

    def test_minimum_levels(self):       # Тест на минимальное количество уровней (1)
        levels = 1
        file(levels)
        with open("yolka.txt", "r") as f:
            content = f.read()

        expected_content = (
            "\n"
            "   W\n"
            "   *\n"
            " TTTTT\n"
            " TTTTT\n"
        )
        self.assertEqual(content, expected_content, "Содержимое файла с уровнем '1' не соответствует ожидаемому")


if __name__ == '__main__':
    unittest.main()