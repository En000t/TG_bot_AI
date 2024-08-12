from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# Функция для выполнения задач в многопоточном режиме
def run_in_thread_pool(func, *args, **kwargs):
    with ThreadPoolExecutor() as executor:
        future = executor.submit(func, *args, **kwargs)
        return future.result()

# Функция для выполнения задач в многопроцессорном режиме (опционально)
def run_in_process_pool(func, *args, **kwargs):
    with ProcessPoolExecutor() as executor:
        future = executor.submit(func, *args, **kwargs)
        return future.result()
