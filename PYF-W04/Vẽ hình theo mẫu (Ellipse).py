import turtle

# Thiết lập màn hình
screen = turtle.Screen()
screen.bgcolor("white")

# Tạo một con rùa tên là "artist"
artist = turtle.Turtle()
artist.speed(0)  # Đặt tốc độ vẽ tối đa

# Khởi tạo bán kính
r = 100

def draw_first_image():
    # Vòng lặp để vẽ hình ellipse
    steps = 0
    while steps < 2:
        artist.circle(r, 90)
        artist.circle(r / 2, 90)
        steps += 1
    screen.onkey(draw_second_image, "Return")
    screen.listen()

def draw_second_image():
    artist.clear()
    artist.penup()
    artist.home()
    artist.pendown()

    # Danh sách màu sắc
    colors = ["red", "green", "blue", "orange", "purple", "yellow"]

    # Vòng lặp để vẽ các hình ellipse xoay
    angle = 0
    while angle < 360:
        artist.color(colors[angle // 60 % len(colors)])
        steps = 0
        while steps < 2:
            artist.circle(r, 90)
            artist.circle(r / 2, 90)
            steps += 1
        artist.right(15)
        angle += 15

    # Ẩn con rùa và hiển thị cửa sổ
    artist.hideturtle()
    turtle.done()

# Vẽ hình thứ nhất
draw_first_image()

# Bắt đầu vòng lặp sự kiện
turtle.done()