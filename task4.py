# 4 - Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) - для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)

from ast import Pow
import datetime
import time
seed = 1

x = time.time() *10000000 %1000


def XorShift128():
    x = time.time_ns() // 1000000 % 1000000
    y = 123
    z = 456
    w = 957
    t = x^(x<<11)
    x = y
    y = z
    z = w
    w = (w^(w>>19)) ^ (t^(t>>8))
    return w % 100 /100

print(XorShift128())

def rnd(min, max):
	max -= min
	return (XorShift128() * max) + min


print(rnd(-10, 10))








