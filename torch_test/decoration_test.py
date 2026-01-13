import time


def time_logging_deco(main_func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        results = main_func(*args, **kwargs)
        end_time = time.time()
        print(f"실행 시간 :{end_time - start_time:.2f}")
        return results
    return wrapper

@time_logging_deco
def testing_deco(sentence:str):
    print(sentence)


if __name__=="__main__":
    testing_deco("안녕")