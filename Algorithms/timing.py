import time

def timing(func):
    def wrapper(*args):
        start_time = time.time()
        result = func(*args)
        print("### Run time %s seconds." % (time.time() - start_time))
        return result
    return wrapper