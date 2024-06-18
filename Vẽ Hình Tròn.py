import turtle

# Thiết lập màn hình
screen = turtle.Screen()
screen.bgcolor("black")

# Tạo một con rùa tên là "artist"
artist = turtle.Turtle()
artist.speed(10)  # Đặt tốc độ vẽ tối đa

# Định nghĩa bán kính
radius = 100

# Vẽ một vòng tròn với màu bên trong
artist.penup()
artist.goto(0, -radius)
artist.pendown()
artist.color("blue")  # Màu viền
artist.begin_fill()
artist.fillcolor("red")  # Màu bên trong
artist.circle(radius)
artist.end_fill()

# Ẩn con rùa và hiển thị cửa sổ
artist.hideturtle()
turtle.done()