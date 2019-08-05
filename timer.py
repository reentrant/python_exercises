import time


def timer(enable=False, display=True, log_file=None, logger=None):
    def decorator(func):
        def wrapper(*args, **kwargs):

            if enable:
                start_time = time.process_time()
                result = func(*args, **kwargs)
                end_time = time.process_time()
                total_time_ms = (end_time - start_time) * 1000

                info_string = '%r : %2.2f ms' % (func.__name__, total_time_ms)

                if display:
                    print(info_string)

                if log_file is not None:
                    with open(log_file, "a") as f:
                        f.write(info_string)

            else:
                result = func(*args, **kwargs)

            return result
        return wrapper
    return decorator
