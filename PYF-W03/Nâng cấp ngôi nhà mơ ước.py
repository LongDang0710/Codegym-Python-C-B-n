import turtle

# Thiết lập màn hình
screen = turtle.Screen()
screen.bgcolor("white")

# Tạo một con rùa tên là "artist"
artist = turtle.Turtle()
artist.speed(10)

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

def draw_circle(turtle, x, y, radius, color, outline_color):
    turtle.penup()
    turtle.goto(x, y - radius)  # Điều chỉnh vị trí bắt đầu vẽ hình tròn
    turtle.pendown()
    turtle.color(outline_color, color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()

def draw_house(turtle):
    # Vẽ thân nhà
    draw_rectangle(turtle, -50, -50, 100, 60, "lightblue")

    # Vẽ mái nhà
    draw_triangle(turtle, -70, 10, 140, "brown")

    # Vẽ cửa ra vào
    draw_rectangle(turtle, -20, -50, 20, 30, "brown")

    # Vẽ cửa sổ trái
    draw_rectangle(turtle, -45, -30, 15, 15, "blue")

    # Vẽ cửa sổ phải
    draw_rectangle(turtle, 20, -30, 15, 15, "blue")

    # Vẽ ống khói
    draw_rectangle(turtle, 30, 10, 10, 30, "gray")
    turtle.penup()
    turtle.goto(35, 40)
    turtle.pendown()
    turtle.forward(10)
    turtle.penup()
    turtle.goto(32, 45)
    turtle.pendown()
    turtle.forward(6)
    turtle.penup()
    turtle.goto(30, 50)
    turtle.pendown()
    turtle.forward(4)

def draw_tree(turtle, x, y, trunk_color, leaf_color1, leaf_color2, leaf_color3):
    # Vẽ thân cây
    draw_rectangle(turtle, x, y, 10, 20, trunk_color)

    # Vẽ lá cây
    draw_triangle(turtle, x - 20, y + 20, 40, leaf_color1)
    draw_triangle(turtle, x - 15, y + 35, 30, leaf_color2)
    draw_triangle(turtle, x - 10, y + 50, 20, leaf_color3)

def draw_taller_tree(turtle, x, y, trunk_color, leaf_color1, leaf_color2, leaf_color3):
    # Vẽ thân cây
    draw_rectangle(turtle, x, y, 10, 40, trunk_color)

    # Vẽ lá cây
    draw_triangle(turtle, x - 30, y + 40, 60, leaf_color1)
    draw_triangle(turtle, x - 25, y + 60, 50, leaf_color2)
    draw_triangle(turtle, x - 20, y + 80, 40, leaf_color3)

def draw_cloud(turtle, x, y):
    # Vẽ đám mây gồm 3 hình tròn với viền màu xanh nhạt
    draw_circle(turtle, x, y, 20, "white", "lightblue")
    draw_circle(turtle, x + 20, y, 20, "white", "lightblue")
    draw_circle(turtle, x + 10, y + 15, 20, "white", "lightblue")

# Vẽ ngôi nhà
draw_house(artist)

# Vẽ các cây thấp bên trái
draw_tree(artist, -200, -100, "gray", "darkgreen", "green", "lightgreen")
draw_tree(artist, -250, -110, "gray", "darkgreen", "green", "lightgreen")

# Vẽ các cây cao bên phải
draw_taller_tree(artist, 200, -100, "gray", "darkgreen", "green", "lightgreen")
draw_taller_tree(artist, 250, -120, "gray", "darkgreen", "green", "lightgreen")

# Vẽ mặt trời
draw_circle(artist, 200, 200, 30, "yellow", "yellow")

# Vẽ đám mây
draw_cloud(artist, -100, 150)
draw_cloud(artist, 50, 150)

# Ẩn con rùa và hiển thị cửa sổ
artist.hideturtle()
turtle.done()