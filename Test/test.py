import unittest
import os
from sors.lab4 import read_graph, find_min_depth

class TestMinimumDepth(unittest.TestCase):

    def setUp(self):
        # Створюємо тестовий вміст для input.txt
        test_input = "1\n1,2\n1,3\n2,4\n2,5\n"

        # Записуємо тестовий вміст у файл input.txt
        with open("input.txt", "w") as file:
            file.write(test_input)

    def tearDown(self):
        # Видаляємо файл input.txt після завершення кожного тесту
        os.remove("input.txt")

    def test_minimum_depth(self):
        root, graph = read_graph("input.txt")
        min_depth = find_min_depth(root, graph)
        self.assertEqual(min_depth, 2)

    def test_empty_tree(self):
        # Створюємо тестовий вміст для input.txt
        test_input = "1\n"

        # Записуємо тестовий вміст у файл input.txt
        with open("input.txt", "w") as file:
            file.write(test_input)

        root, graph = read_graph("input.txt")
        min_depth = find_min_depth(root, graph)
        self.assertEqual(min_depth, 1)

if __name__ == '__main__':
    unittest.main()
