import turtle

# Thiết lập màn hình
screen = turtle.Screen()
screen.bgcolor("skyblue")

# Tạo một con rùa tên là "artist"
artist = turtle.Turtle()
artist.speed(10)  # Đặt tốc độ vẽ tối đa


def draw_rectangle(turtle, x, y, width, height, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()


def draw_triangle(turtle, x, y, length, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(length)
        turtle.left(120)
    turtle.end_fill()
    turtle.penup()


def draw_circle(turtle, x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()


def draw_tree(turtle, x, y):
    # Vẽ thân cây
    draw_rectangle(turtle, x, y, 20, 60, "brown")

    # Vẽ lá cây
    draw_triangle(turtle, x - 30, y + 60, 80, "green")
    draw_triangle(turtle, x - 25, y + 90, 70, "green")
    draw_triangle(turtle, x - 20, y + 120, 60, "green")


# Vẽ thân nhà
draw_rectangle(artist, -250, -100, 200, 150, "green")

# Vẽ mái nhà
draw_triangle(artist, -270, 50, 240, "brown")

# Vẽ cửa ra vào
draw_rectangle(artist, -200, -100, 40, 70, "red")

# Vẽ cửa sổ trái
draw_rectangle(artist, -230, -10, 30, 30, "blue")

# Vẽ cửa sổ phải
draw_rectangle(artist, -140, -10, 30, 30, "blue")

# Vẽ mặt trời
draw_circle(artist, 200, 200, 50, "yellow")

# Vẽ cây, không trùng lặp
draw_tree(artist, 50, -200)
draw_tree(artist, 150, -200)
draw_tree(artist, 250, -200)

# Ẩn con rùa và hiển thị cửa sổ
artist.hideturtle()
turtle.done()