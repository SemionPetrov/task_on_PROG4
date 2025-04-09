from laboroty1.exceptions_for_gen_bin_tree import *

def validate_input(Root, height):
    if not isinstance(Root, (int, float)):
        raise InvalidRootException(Root)
    if not isinstance(height, int) or height < 0:
        raise InvalidHeightException(height)

def gen_bin_tree_array(Root=17, height=4, L_branch=lambda x: (x - 4) ** 2, R_branch=lambda x: (x + 3) * 2):
    validate_input(Root, height)
    # Размер массива для дерева высоты `height`
    max_nodes = 2 ** (height + 1) - 1
    tree = [None] * max_nodes
    tree[0] = Root

    for i in range(2 ** height):  # Проходим по всем узлам
        if tree[i] is not None:
            left_index = 2 * i + 1
            right_index = 2 * i + 2

            if left_index < max_nodes:
                tree[left_index] = L_branch(tree[i])

            if right_index < max_nodes:
                tree[right_index] = R_branch(tree[i])

    return tree


if __name__ == "__main__":
    try:
        print(gen_bin_tree_array(Root=17, height=2))
    except Exception as e:
        print(f"Error: {e}")