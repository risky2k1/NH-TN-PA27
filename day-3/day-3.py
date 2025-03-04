import turtle
from turtle import Screen, Turtle
import math

# Khởi tạo (Tạo ra) 1 màn hình
man_hinh = Screen()
man_hinh.setup(500,500)

#kHởi tạo các obj rùa
con_rua_1 = Turtle()
# Điều chỉnh thuộc tính shape
con_rua_1.shape('turtle')
# Điều chỉnh màu sắc
con_rua_1.color('red')
# Điều khiển rùa đi thẳng về trước
con_rua_1.forward(100)
# Điều khiển rùa đi lùi
con_rua_1.backward(200)
# Điều khiển rùa quay đầu về bên trái
con_rua_1.left(90)
# Điều khiển rùa quay đầu sang phải
con_rua_1.right(45)

# Tạo ra 1 con rùa số 2, cho rùa 2 vẽ hình vuông
rua_2 = Turtle()

rua_2.color('green')

for i in range(0,4):
    rua_2.forward(200)
    rua_2.right(90)

    # Tạo rùa 3 vẽ mái cho ngồi nhà
rua_3 = Turtle()
rua_3.shape('circle')
rua_3.color('yellow')

rua_3.left(45)
rua_3.forward(math.sqrt(20000))
rua_3.right(90)
rua_3.forward(math.sqrt(20000))

# tạo rùa 4 và vẽ hình tròn
# rua_4 = Turtle()

# for i in range(0,720):
#     rua_4.forward(1/2)
#     rua_4.left(1/2)

rua_5 = Turtle()
rua_5.penup()
rua_5.goto(200/3,-200)
rua_5.pendown()

rua_5.left(90)
rua_5.forward(50)
rua_5.right(90)
rua_5.forward(200/3)
rua_5.right(90)
rua_5.forward(50)

man_hinh.exitonclick()



