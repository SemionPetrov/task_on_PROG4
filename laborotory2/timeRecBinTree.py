import time

def gen_bin_tree(root=10, height=10, L_branch=lambda x: (x - 4) ** 2, R_branch=lambda x: (x + 3) * 2):
    if height == 0:
        return {'value': root, 'left': None, 'right': None}
    else:
        left = gen_bin_tree(L_branch(root), height - 1, L_branch, R_branch)
        right = gen_bin_tree(R_branch(root), height - 1, L_branch, R_branch)
        return {'value': root, 'left': left, 'right': right}

def measure_execution_time():
    root = 10
    heights = range(9, 19)  # Высоты от 9 до 19
    execution_times = []

    for height in heights:
        # Используем time.perf_counter() для максимальной точности
        start_time = time.perf_counter()
        gen_bin_tree(root=root, height=height)
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
    for height, (exec_time_s, exec_time_ms, exec_time_us) in zip(range(9, 19), execution_times):
        print(f"Height: {height}, Execution Time: "
              f"{exec_time_s:.6f} s ({exec_time_ms:.6f} ms, {exec_time_us:.6f} μs)")