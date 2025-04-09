from laborotory1.exceptions_for_gen_bin_tree import *

def validate_input(Root, height):
    if not isinstance(Root, (int, float)):
        raise InvalidRootException(Root)
    if not isinstance(height, int) or height < 0:
        raise InvalidHeightException(height)

def gen_bin_tree_iterative(Root=17, height=4, L_branch=lambda x:(x-4)**2, R_branch=lambda x: (x+3) * 2) -> dict:
    validate_input(Root, height)
    if height == 0:
        return {'value': Root, 'left': None, 'right': None}

    # Создаем корень дерева
    root = {'value': Root, 'left': None, 'right': None}

    # Список узлов для текущего уровня
    current_level = [root]

    for _ in range(height):
        next_level = []
        for node in current_level:
            left_value = L_branch(node['value'])
            right_value = R_branch(node['value'])

            # Создаем левого и правого потомков
            left_child = {'value': left_value, 'left': None, 'right': None}
            right_child = {'value': right_value, 'left': None, 'right': None}

            # Присваиваем потомков текущему узлу
            node['left'] = left_child
            node['right'] = right_child

            # Добавляем потомков в следующий уровень
            next_level.append(left_child)
            next_level.append(right_child)

        # Переходим к следующему уровню
        current_level = next_level

    # Возвращаем корень дерева
    return root


if __name__ == "__main__":
    try:
        print(gen_bin_tree_iterative(Root=17, height=-2))

    except Exception as e:
        print(f"Error: {e}")