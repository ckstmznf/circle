import turtle as t
import time
from math import sqrt

# t.bgcolor("black")
t.shapesize(1,1,1)
t.speed(20)
t.width(1)
t.st()


o_x = int(t.textinput("", "원의 중심에 x좌표를 입력하세요 > "))
o_y = int(t.textinput("", "원의 중심에 y좌표를 입력하세요 > "))
r = int(t.textinput("", "원의 반지름 입력하세요 > "))


# x축 y축을 그린다.
t.goto(-500, 0) # x축 가장 왼쪽 부터
t.goto(500, 0) # x축 가장 오른쪽 까지
t.pu()
t.goto(0, 500) # y축 가장 위부터
t.pd()
t.goto(0, -500) #y축 가장 아래까지


# 원의 중심으로 이동
t.pu()
t.goto(o_x, o_y)
t.dot(3, "red")
t.pu()

t.speed(0)
t.width(1)
t.color("red")



# x축 범위만큼 반복하며 식에 대입해 y의 값을 찾은뒤 점을 찍는다.
for x in range(o_x - r, o_x + r + 1, 2):
    y = o_y + sqrt(r **  2 - (x - o_x) ** 2)
    t.goto(x, y)
    # t.dot(3, "red")

    t.pd()
    print(f"({x}, {y})")

# 다시 x축 범위만큼 반복하여 y의 값을 찾아 점을 찍는다. 이때 y는 음의 제곱근이다.
for x in reversed(range(o_x - r, o_x + r + 1, 2)):
    y = o_y - sqrt(r **  2 - (x - o_x) ** 2)
    t.goto(x, y)
    # t.dot(3, "red")
    print(f"({x}, {y})")


# 반지름을 그린다.
t.width(3)
t.goto(o_x, o_y)
t.dot(3, "blue")

# 텍스트
t.up()
t.left(135)
t.forward(30)
t.left(45)
t.forward(20)
t.write(r)

t.ht()
t.mainloop()