import functools
import time

def retry(maxTries: int, timeout: float):
    """Retry function if it raises an exeption"""
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            failed_cnt = 0
            while failed_cnt < maxTries:
                print(f"% {failed_cnt} fails", flush=True)
                try:
                    rc = f(*args, **kwargs)
                    return rc
                except:
                    failed_cnt += 1
                    if failed_cnt == maxTries:
                        raise
                    time.sleep(timeout)
            return rc
        return wrapper
    return decorator

@retry(20, 0.1)
def func(a, b, c=[1, 0, 0, 0, 0]):
    print(a, b, c, flush=True)
    return 450 / c.pop() 

print(func('a', b={5: 0}))
