import turtle

# Thiết lập màn hình
screen = turtle.Screen()
screen.bgcolor("skyblue")

# Tạo một con rùa tên là "artist"
artist = turtle.Turtle()
artist.speed(5)  # Đặt tốc độ vẽ


# Hàm vẽ hình chữ nhật
def draw_rectangle(turtle, width, height, color):
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()


# Hàm vẽ hình tam giác
def draw_triangle(turtle, length, color):
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(3):
        turtle.forward(length)
        turtle.left(120)
    turtle.end_fill()


# Hàm vẽ hình tròn
def draw_circle(turtle, radius, color):
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.circle(radius)
    turtle.end_fill()


# Hàm di chuyển con rùa đến vị trí mới
def move_turtle(turtle, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


# Vẽ ngôi nhà
def draw_house():
    # Vẽ phần thân nhà
    move_turtle(artist, -100, -150)
    artist.color("black")
    draw_rectangle(artist, 200, 150, "yellow")

    # Vẽ mái nhà
    move_turtle(artist, -120, 0)
    artist.color("black")
    draw_triangle(artist, 240, "red")

    # Vẽ cửa chính
    move_turtle(artist, -30, -150)
    artist.color("black")
    draw_rectangle(artist, 60, 100, "brown")

    # Vẽ cửa sổ bên trái
    move_turtle(artist, -80, -50)
    artist.color("black")
    draw_rectangle(artist, 40, 40, "blue")

    # Vẽ cửa sổ bên phải
    move_turtle(artist, 40, -50)
    artist.color("black")
    draw_rectangle(artist, 40, 40, "blue")


# Vẽ cây cối
def draw_tree(x, y):
    # Vẽ thân cây
    move_turtle(artist, x, y)
    artist.color("black")
    draw_rectangle(artist, 20, 60, "brown")

    # Vẽ lá cây
    move_turtle(artist, x - 30, y + 60)
    artist.color("black")
    draw_triangle(artist, 80, "green")
    move_turtle(artist, x - 25, y + 90)
    artist.color("black")
    draw_triangle(artist, 70, "green")
    move_turtle(artist, x - 20, y + 120)
    artist.color("black")
    draw_triangle(artist, 60, "green")


# Vẽ mặt trời
def draw_sun():
    move_turtle(artist, 200, 200)
    artist.color("black")
    draw_circle(artist, 50, "yellow")


# Vẽ mây
def draw_cloud(x, y):
    move_turtle(artist, x, y)
    artist.color("black")
    draw_circle(artist, 20, "white")
    move_turtle(artist, x + 25, y + 10)
    draw_circle(artist, 20, "white")
    move_turtle(artist, x + 50, y)
    draw_circle(artist, 20, "white")
    move_turtle(artist, x + 15, y - 10)
    draw_circle(artist, 20, "white")
    move_turtle(artist, x + 35, y - 10)
    draw_circle(artist, 20, "white")


# Vẽ người
def draw_person(x, y):
    # Đầu
    move_turtle(artist, x, y)
    artist.color("black")
    draw_circle(artist, 10, "pink")

    # Thân
    move_turtle(artist, x, y - 10)
    artist.pendown()
    artist.setheading(270)  # Hướng xuống dưới
    artist.forward(40)

    # Tay trái
    move_turtle(artist, x, y - 20)
    artist.setheading(180)  # Hướng sang trái
    artist.forward(20)

    # Tay phải
    move_turtle(artist, x, y - 20)
    artist.setheading(0)  # Hướng sang phải
    artist.forward(20)

    # Chân trái
    move_turtle(artist, x, y - 50)
    artist.setheading(225)  # Hướng xuống trái
    artist.forward(20)

    # Chân phải
    move_turtle(artist, x, y - 50)
    artist.setheading(315)  # Hướng xuống phải
    artist.forward(20)


# Vẽ toàn bộ khung cảnh
def draw_scene():
    draw_house()
    draw_tree(-150, -150)
    draw_tree(150, -150)
    draw_sun()
    draw_cloud(-150, 150)
    draw_cloud(50, 180)
    draw_person(-50, -120)
    draw_person(100, -120)


# Gọi hàm vẽ toàn bộ khung cảnh
draw_scene()

# Ẩn con rùa và hiển thị cửa sổ
artist.hideturtle()
turtle.done()