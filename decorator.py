import functools
import time

"""
A decorator without arguments
"""
def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        rc = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return rc
    return wrapper_timer


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

waste_some_time(100)
# Finished 'waste_some_time' in 0.3974 secs


"""
A decorator with arguments
"""
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                rc = func(*args, **kwargs)
            return rc
        return wrapper_repeat
    return decorator_repeat


@repeat(2)
def cheer_up(name):
    print(f"{name}, you're the best!")

cheer_up('Vi')
