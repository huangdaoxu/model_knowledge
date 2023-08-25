import time

from concurrent.futures import as_completed, ThreadPoolExecutor
from functools import wraps


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper


def pool_requests(funcs, max_workers=20, timeout=10):
    pool = ThreadPoolExecutor(max_workers=max_workers)
    tasks = list()
    for func in funcs:
        tasks.append(pool.submit(func))

    for task in as_completed(tasks, timeout=timeout):
        yield task.result()
