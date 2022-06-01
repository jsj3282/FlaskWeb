def check(func):
    def wrapper():  # 호출할 함수를 감싸는 함수
        print(func.__name__, "함수 시작")  # __name__으로 함수 이름 출력
        func()  # 매개변수로 받은 함수를 호출
        print(func.__name__, "함수 끝")

    return wrapper  # wrapper 함수 반환


def hello():
    print("hello")


def world():
    print("world")


trace_hello = check(hello)
trace_hello()
trace_world = check(world)
trace_world()
