from laboroty1.exceptions_for_gen_bin_tree import *

def validate_input(Root, height):
    if not isinstance(Root, (int, float)):
        raise InvalidRootException(Root)
    if not isinstance(height, int) or height < 0:
        raise InvalidHeightException(height)

def gen_bin_tree_list_of_lists(Root=17, height=4, L_branch=lambda x: (x - 4) ** 2, R_branch=lambda x: (x + 3) * 2):
    validate_input(Root, height)
    if height == 0:
        return [Root, None, None]

    # Создаем корень дерева
    tree = [Root, None, None]

    # Очередь для обхода узлов
    queue = [(tree, 0)]  # (текущий_узел, текущая_высота)

    while queue:
        current_node, current_height = queue.pop(0)

        if current_height < height:
            # Вычисляем значения левого и правого потомков
            left_value = L_branch(current_node[0])
            right_value = R_branch(current_node[0])

            # Создаем левого потомка
            current_node[1] = [left_value, None, None]
            queue.append((current_node[1], current_height + 1))

            # Создаем правого потомка
            current_node[2] = [right_value, None, None]
            queue.append((current_node[2], current_height + 1))

    return tree


if __name__ == "__main__":
    try:
        print(gen_bin_tree_list_of_lists(Root=17, height=2))

    except Exception as e:
        print(f"Error: {e}")