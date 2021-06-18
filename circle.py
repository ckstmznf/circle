import turtle as t
import time
from math import sqrt

# 팬의 기본 설정
t.shapesize(1,1,1) # 팬(화살표)의 크기를 1,1,1로 설정한다.
t.speed(20) #팬이 이동하동 속도를 20으로 설정
t.width(1) # 팬(브러쉬)의 크기를 1로 설정


o_x = int(t.textinput("", "원의 중심에 x좌표를 입력하세요 > ")) #원의 중심에 x좌표를 입력받는다.
o_y = int(t.textinput("", "원의 중심에 y좌표를 입력하세요 > ")) #원의 중심에 y좌표를 입력받는다.
r = int(t.textinput("", "원의 반지름 입력하세요 > ")) #원의 반지름 입력받는다.


# x축 y축을 그린다.
t.goto(-500, 0) # x축 가장 왼쪽 부터
t.goto(500, 0) # x축 가장 오른쪽 까지
t.pu() # 팬을 들어 올린다. 만약 팬을 올리지 않는다면 이동하면서 캔버스에 그려질것이다.
t.goto(0, 500) # y축 가장 위부터
t.pd() #팬을 내린다. 
t.goto(0, -500) #y축 가장 아래까지


t.color("red") # 팬의 색을 red로 변경



# x축 범위만큼 반복하며 식에 대입해 y의 값을 찾은뒤 점을 찍는다.
# 이때의 범위는 원의 중심의 x값에서 반지름을 뺀 값부터, 원의 중심의 x값에서 반지름을 더한 값까지이다.
# 이때 원이 그려지는 속도를 위해 x값을 2씩 증가시키겠다.
for x in range(o_x - r, o_x + r + 1, 2):
    y = o_y + sqrt(r **  2 - (x - o_x) ** 2)
    t.goto(x, y)
    # t.dot(3, "red")

    t.pd()
    print(f"({x}, {y})")


# 다시 x축 범위만큼 반복하여 y의 값을 찾아 점을 찍는다. 이때 y값은 음의 제곱근이다.
for x in reversed(range(o_x - r, o_x + r + 1, 2)):
    y = o_y - sqrt(r **  2 - (x - o_x) ** 2)
    t.goto(x, y)
    # t.dot(3, "red")
    print(f"({x}, {y})")


# 반지름을 그린다.
t.width(3)
t.goto(o_x, o_y) # 현재 위치에서 중심까지 이동한다. 원의 한점에서 원의 중심을 이은 선분 == 원의 반지름


# 텍스트
t.up()
t.left(135)
t.forward(30)
t.left(45)
t.forward(20)
t.write(r)

t.ht()
t.mainloop() # 화면이 꺼지는걸 방지한다.