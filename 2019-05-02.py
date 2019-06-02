"""
判断输入的边长能否构成三角形
如果能则计算出三角形的周长和面积

Version: 0.1
Author: 苏仁君
"""
# import math
#
# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))
# if a + b > c and a + c > b and b + c > a:
#     print('周长:%f' % (a + b + c))
#     p = (a + b + c) / 2
#     area = math.sqrt(p * (p - a) * (p - b) * (p - c))
#     print("面积:%f" % (area))
# else:
#     print("不能构成三角形")

"""
循环结构
用for循环实现1~100之间的偶数求和
"""
sum = 0
for x in range(1, 100 ,2):
    sum += x
print(sum)

"""
打印各种三角形的图案
*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********

    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""
row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()


for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()

row = int(input("请输入行数:"))
for i in range(row):
    if( i <= row//2):
        for j in range(row - i - 1):
            print(' ', end='')
        for x in range(2 * i + 1):
            print('*', end='')
    else:
        for a in range(i - ((row // 2) - 2)):
            print(' ', end='')
        for b in range(4*(row//2 +1) - 2*(i+1) - 1):
            print('*', end='')
    print()
