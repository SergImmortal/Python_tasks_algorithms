import time

def timing(func):
    def wrapper(*args):
        start_time = time.time()
        result = func(*args)
        print("\033[96m### Run time %s seconds. \033[0m" % (time.time() - start_time))
        return result
    return wrapper