import time

def timing(func):
    def wrapper(*args):
        start_time = time.time()
        result = func(*args)
        print("\033[96m### Function "+ func.__name__ +"() run time %s seconds. \033[0m" % (time.time() - start_time))
        return result
    return wrapper