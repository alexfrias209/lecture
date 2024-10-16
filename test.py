import random
import ipdb


ipdb.set_trace()


def func1(a, b):
    print(f"In func1: a={a}, b={b}")
    result = func2(a + 17, b * 2)
    return result


def func2(c, d):
    print(f"In func2: c={c}, d={d}")
    result = func3(c - 1, d / 2)
    return result


def func3(e, f):
    print(f"In func3: e={e}, f={f}")
    return e + f


counter = 0
x = 3
y = 17
ipdb.set_trace()
result = func1(x, y)


for i in range(1000):
    if counter == 1:
        break
    print(f"Loop 3: {i}")


for i in range(1219):
    if i % 53 == 0:  
        print(f"Number with remainder 0: {i}")


# don't forget to make hello variable in interactive ipdb session
ipdb.set_trace()
print(hello)


