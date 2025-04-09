from collections import deque
from laboroty1.exceptions_for_gen_bin_tree import *

def validate_input(Root, height):
    if not isinstance(Root, (int, float)):
        raise InvalidRootException(Root)
    if not isinstance(height, int) or height < 0:
        raise InvalidHeightException(height)

def gen_bin_tree_deque(Root=17, height=4, L_branch=lambda x: (x - 4) ** 2, R_branch=lambda x: (x + 3) * 2) -> dict:
    validate_input(Root, height)
    if height == 0:
        return {'value': Root, 'left': None, 'right': None}

    # Создаем корень дерева
    root = {'value': Root, 'left': None, 'right': None}

    # Очередь для обхода узлов
    queue = deque([(root, None, None)])  # (текущий_узел, родительский_узел, позиция ('left' или 'right'))

    current_height = 0
    while queue and current_height < height:
        level_size = len(queue)
        for _ in range(level_size):
            node, parent, position = queue.popleft()

            # Вычисляем значения левого и правого потомков
            left_value = L_branch(node['value'])
            right_value = R_branch(node['value'])

            # Создаем левого потомка
            left_child = {'value': left_value, 'left': None, 'right': None}
            node['left'] = left_child
            queue.append((left_child, node, 'left'))

            # Создаем правого потомка
            right_child = {'value': right_value, 'left': None, 'right': None}
            node['right'] = right_child
            queue.append((right_child, node, 'right'))

        # Увеличиваем текущую высоту
        current_height += 1

    return root

if __name__ == "__main__":
    try:
        print(gen_bin_tree_deque(Root=17, height=1))

    except Exception as e:
        print(f"Error: {e}")