import turtle

# có sẵn GUI (Graphic User Interface)

# Tạo ra màn vẽ
# Truy cập class Screen từ trong file hay thư viện turle
# Khởi tạo 1 Obj màn hình
screen = turtle.Screen()
# Thiết lập kich thước cho màn hình
screen.setup(width=400, height=200)

#tạo ra các obj rùa từ class Turtle
turtle_1 = turtle.Turtle()
turtle_1.color('red')
turtle_1.shape('classic')
# Di chuyển về trước 50 đơn vị
turtle_1.forward(50)
# Quay trái 90 độ
turtle_1.left(90)
# Quay phải 45 độ
turtle_1.right(45)
# lùi 50 đơn vị
turtle_1.backward(50)

turtle_2 = turtle.Turtle()
turtle_2.color('yellow')
turtle_2.shape('circle')

# Vẽ hình vuông - Cách 1
# turtle_2.forward(100)
# turtle_2.left(90)
# turtle_2.forward(100)
# turtle_2.left(90)
# turtle_2.forward(100)
# turtle_2.left(90)
# turtle_2.forward(100)

# Vẽ hình vuông - Cách 2
for i in range(0,4):
    turtle_2.forward(100)
    turtle_2.left(90)

turtle_3 = turtle.Turtle()
turtle_3.color('green')

# Vẽ hình tròn
for i in range(0, 360):
    turtle_3.forward(1)
    turtle_3.left(1)

turtle_3.speed(0)


# Chạy vòng lặp để giữ màn hình (screen) luôn chạy
screen.mainloop()

