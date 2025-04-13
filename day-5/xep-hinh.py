from turtle import Screen, Turtle

man_hinh = Screen()

WIDTH = 450
HEIGHT = 720

man_hinh.setup(WIDTH+100, HEIGHT+100)

BLOCK_SIZE = 45

SHAPES = [
    # I
    [1, 1, 1, 1],
    # O
    [
        [1, 1],
        [1, 1]
    ],
    # L
    [
        [1,0,0],
        [1,1,1]
    ],
    # Z
    [
        [1,0],
        [1,1],
        [0,1]
    ],
    # T
    [
        [0,1,0],
        [1,1,1]
    ]
]


man_hinh.exitonclick()
