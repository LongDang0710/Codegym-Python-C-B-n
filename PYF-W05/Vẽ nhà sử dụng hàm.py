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

# Hàm di chuyển con rùa đến vị trí mới
def move_turtle(turtle, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

# Vẽ phần thân nhà
move_turtle(artist, -100, -150)
artist.color("black")
draw_rectangle(artist, 200, 150, "yellow")

# Vẽ mái nhà
move_turtle(artist, -120, 0)
artist.color("black")
draw_rectangle(artist, 240, 60, "red")

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

# Ẩn con rùa và hiển thị cửa sổ
artist.hideturtle()
turtle.done()