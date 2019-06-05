""""
    函数
"""
# 在参数名前面的*表示args是一个可变参数
# 即在调用add函数时可以传入0个或多个参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total
print(add(1, 2))

from module1 import foo
foo()
from module2 import foo
foo()

import module1 as m1
import module2 as m2
m1.foo()
m2.foo()

import module3

#练习1：实现计算求最大公约数和最小公倍数的函数。
def cal(x, y):
    (x, y) = (x, y) if x > y else(y, x)
    for factor in range(x , 0 -1):
        if x % factor == 0 and y % factor == 0:
            return factor
def lcm(x, y):
    return x * y // cal(x , y)

#练习2：实现判断一个数是不是回文数的函数。
def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num

def foo():
    a = 200
    print(a)  # 200


if __name__ == '__main__':
    a = 100
    foo()
    print(a)  # 100

def foo():
    global a # global关键字来指示foo函数中的变量a来自于全局作用域，如果全局作用域中没有a，那么下面一行的代码就会定义变量a并将其置于全局作用域
    a = 200
    print(a)  # 200


if __name__ == '__main__':
    a = 100  # 定义一个全局变量a
    foo()    # 拿到全局变量a 并修改全局变量a
    print(a)  # 200