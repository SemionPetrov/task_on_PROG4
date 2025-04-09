import time

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

def measure_execution_time():
    root = 10
    heights = range(9, 19)  # Высоты от 9 до 19
    execution_times = []

    for height in heights:
        # Используем time.perf_counter() для максимальной точности
        start_time = time.perf_counter()
        gen_bin_tree_iterative(Root=root, height=height)
        end_time = time.perf_counter()

        # Переводим время в секунды, миллисекунды, микросекунды, наносекунды и пикосекунды
        elapsed_time_s = end_time - start_time                          # Секунды
        elapsed_time_ms = elapsed_time_s * 1e3                         # Миллисекунды
        elapsed_time_us = elapsed_time_ms * 1e3                        # Микросекунды


        execution_times.append((elapsed_time_s, elapsed_time_ms, elapsed_time_us,))

    return execution_times

if __name__ == '__main__':
    execution_times = measure_execution_time()

    print("Execution Times:")
    for height, (exec_time_s, exec_time_ms, exec_time_us) in zip(range(9, 22), execution_times):
        print(f"Height: {height}, Execution Time: "
              f"{exec_time_s:.6f} s ({exec_time_ms:.6f} ms, {exec_time_us:.6f} μs)")