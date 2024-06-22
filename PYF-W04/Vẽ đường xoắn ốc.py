import turtle

# Thiết lập màn hình
screen = turtle.Screen()
screen.bgcolor("white")

# Tạo một con rùa tên là "artist"
artist = turtle.Turtle()
artist.speed(0)  # Đặt tốc độ vẽ tối đa

# Lưu vị trí ban đầu
start_pos = artist.pos()

# Nhập vào giá trị khoảng cách từ người dùng
max_distance = float(input("Nhập vào giá trị khoảng cách tối đa: "))

# Khởi tạo khoảng cách di chuyển
d = 1

# Vòng lặp để vẽ đường xoắn ốc
while True:
    artist.forward(d)
    artist.left(20)
    d += 0.5  # Tăng giá trị khoảng cách để mở rộng vòng xoắn

    # Kiểm tra khoảng cách từ vị trí hiện tại đến vị trí ban đầu
    if artist.distance(start_pos) > max_distance:
        break

# Ẩn con rùa và hiển thị cửa sổ
artist.hideturtle()
turtle.done()