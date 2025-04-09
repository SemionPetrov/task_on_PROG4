def gen_bin_tree_iterative(Root=17, height=4, L_branch=lambda x:(x-4)**2, R_branch=lambda x: (x+3) * 2) -> dict:
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
    tree = gen_bin_tree_iterative(Root=17, height=2)
    print(tree)