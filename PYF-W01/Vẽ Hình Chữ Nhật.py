import turtle

# Thiết lập màn hình
screen = turtle.Screen()
screen.bgcolor("black")

# Tạo một con rùa tên là "artist"
artist = turtle.Turtle()
artist.speed(10)  # Đặt tốc độ vẽ tối đa

# Định nghĩa kích thước hình chữ nhật
width = 200
height = 100

# Vẽ một hình chữ nhật với màu bên trong
artist.penup()
artist.goto(-width // 2, -height // 2)
artist.pendown()
artist.color("blue")  # Màu viền
artist.begin_fill()
artist.fillcolor("red")  # Màu bên trong

# Vẽ hình chữ nhật
for _ in range(2):
    artist.forward(width)
    artist.left(90)
    artist.forward(height)
    artist.left(90)

artist.end_fill()

# Ẩn con rùa và hiển thị cửa sổ
artist.hideturtle()
turtle.done()