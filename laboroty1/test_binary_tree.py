import unittest
# Импортируем все реализации генерации дерева
from laboroty1.NoRecBinaryTree.noRecBinaryTree_iterative import gen_bin_tree_iterative
from laboroty1.NoRecBinaryTree.noRecBinary_deque import gen_bin_tree_deque
from laboroty1.NoRecBinaryTree.noRecBinaryTree_Array import gen_bin_tree_array
from laboroty1.NoRecBinaryTree.noRecBinaryTree_LoL import gen_bin_tree_list_of_lists
from laboroty1.RecBinaryTree.RecBinaryTree import gen_bin_tree
# Импортируем пользовательские исключения
from laboroty1.exceptions_for_gen_bin_tree import InvalidHeightException, InvalidRootException

class TestBinaryTree(unittest.TestCase):
    # Тесты для итеративной версии (словарь)
    def test_iterative_height_0(self):
        tree = gen_bin_tree_iterative(Root=5, height=0)
        expected = {'value': 5, 'left': None, 'right': None}
        self.assertEqual(tree, expected)

    def test_iterative_height_1(self):
        tree = gen_bin_tree_iterative(Root=17, height=1)
        expected = {
            'value': 17,
            'left': {'value': 169, 'left': None, 'right': None},
            'right': {'value': 40, 'left': None, 'right': None}
        }
        self.assertEqual(tree, expected)

    # Тесты для версии с deque
    def test_deque_height_0(self):
        tree = gen_bin_tree_deque(Root=5, height=0)
        expected = {'value': 5, 'left': None, 'right': None}
        self.assertEqual(tree, expected)

    def test_deque_height_1(self):
        tree = gen_bin_tree_deque(Root=17, height=1)
        expected = {
            'value': 17,
            'left': {'value': 169, 'left': None, 'right': None},
            'right': {'value': 40, 'left': None, 'right': None}
        }
        self.assertEqual(tree, expected)

    # Тесты для версии с массивом
    def test_array_height_0(self):
        tree = gen_bin_tree_array(Root=5, height=0)
        expected = [5, None, None]
        self.assertEqual(tree, expected)

    def test_array_height_1(self):
        tree = gen_bin_tree_array(Root=17, height=1)
        expected = [17, 169, 40, 15129, 306, 1296, 86]
        self.assertEqual(tree, expected)

    # Тесты для версии со списком списков
    def test_list_of_lists_height_0(self):
        tree = gen_bin_tree_list_of_lists(Root=5, height=0)
        expected = [5, None, None]
        self.assertEqual(tree, expected)

    def test_list_of_lists_height_1(self):
        tree = gen_bin_tree_list_of_lists(Root=17, height=1)
        expected = [
            17,
            [169, [15129, None, None], [306, None, None]],
            [40, [1296, None, None], [86, None, None]]
        ]
        self.assertEqual(tree, expected)

    # Тесты для рекурсивной версии
    def test_recursive_height_0(self):
        tree = gen_bin_tree(Root=5, height=0)
        expected = {'value': 5, 'left': None, 'right': None}
        self.assertEqual(tree, expected)

    def test_recursive_height_1(self):
        tree = gen_bin_tree(Root=17, height=1)
        expected = {
            'value': 17,
            'left': {'value': 169, 'left': None, 'right': None},
            'right': {'value': 40, 'left': None, 'right': None}
        }
        self.assertEqual(tree, expected)

    # Тесты на обработку ошибок
    def test_invalid_height(self):
        with self.assertRaises(InvalidHeightException):
            gen_bin_tree_iterative(Root=17, height=-1)

    def test_invalid_root(self):
        with self.assertRaises(InvalidRootException):
            gen_bin_tree_iterative(Root="invalid", height=2)

if __name__ == "__main__":
    unittest.main()