import time

def logging_deco(main_func):
    def wrapper(*args, **kwargs):
        print(f"{main_func.__name__}의 doc-string : {main_func.__doc__}")
        start_time = time.time()
        result = main_func(*args, **kwargs)
        end_time = time.time()
        print(f"{main_func.__name__}의 실행 시간 : {end_time - start_time:.4f}")
        return result
    return wrapper


@logging_deco
def test_func(name:str, age:int):
    """
    입력된 인물의 이름과 나이를 출력합니다.
    """
    print(f"{name}의 나이는 {age}세 입니다.")



def main():
    name = "이영우"
    age = 31
    test_func(name, age)

    name = "김동건"
    age = 312
    test_func(name, age)

    name = "이소영"
    age = 31
    test_func(name, age)

    name = "이스응"
    age = 31
    test_func(name, age)


if __name__ == "__main__":
    p = "git rebase test"
    print(p)
    main()
