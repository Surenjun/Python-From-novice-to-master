"""
  变量命名
  int()：将一个数值或字符串转换成整数，可以指定进制。
  float()：将一个字符串转换成浮点数。
  str()：将指定的对象转换成字符串形式，可以指定编码。
  chr()：将整数转换成该编码对应的字符串（一个字符）。
  ord()：将字符串（一个字符）转换成对应的编码（整数）。

  将华氏温度转换为摄氏温度
  F = 1.8C + 32
  Version: 0.1
  Author: Surenjun
"""
f = float(input('请输入华氏温度:'))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))

"""
 分段函数求值

        3x - 5  (x > 1)
 f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
"""

x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3

if x > 1:
    y = 3 * x - 5
else:
    if x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))
print('f(%.2f) = %.2f' % (x, y))