import turtle as t
import math, time

# t.bgcolor("black")


def axis():
    t.speed(10)
    t.width(2)
    t.st()
    t.pd()
    t.goto(-500, 0)
    t.goto(500, 0)
    t.pu()
    t.goto(0, 500)
    t.pd()
    t.goto(0, -500)

o_x = int(input("원의 중심에 x좌표를 입력하세요 > "))
o_y = int(input("원의 중심에 y좌표를 입력하세요 > "))
r = int(input("원의 반지름 입력하세요 > "))

# t.shape("circle")

time.sleep(3)
t.shapesize(1,1,1)

axis() # x축 y축을 그린다.

t.pu()
t.goto(o_x, o_y)
t.dot(3, "red")
t.pu()
t.width(1)

t.color("red")
for x in range(o_x - r, o_x + r + 1, 2):
    y = o_y + math.sqrt(r **  2 - (x - o_x) ** 2)
    t.goto(x, y)
    t.pd()
    print(x, y)

for x in reversed(range(o_x - r, o_x + r + 1, 2)):
    y = o_y - math.sqrt(r **  2 - (x - o_x) ** 2)
    t.goto(x, y)
    print(x, y)

t.width(3)
t.goto(o_x, o_y)
t.dot(3, "blue")

t.ht()
t.mainloop()