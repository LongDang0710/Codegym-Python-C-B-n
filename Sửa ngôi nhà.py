import turtle

# Thiết lập màn hình
screen = turtle.Screen()
screen.bgcolor("skyblue")

# Tạo một con rùa tên là "artist"
artist = turtle.Turtle()
artist.speed(10)  # Đặt tốc độ vẽ tối đa

# Các biến màu sắc
house_color = "green"
roof_color = "brown"
door_color = "red"
window_color = "blue"
sun_color = "yellow"
tree_trunk_color = "brown"
tree_leaves_color = "green"

# Các biến kích thước
house_width = 200
house_height = 150
roof_length = 240
door_width = 40
door_height = 70
window_size = 30
sun_radius = 50
tree_trunk_width = 20
tree_trunk_height = 60
tree_leaves_lengths = [80, 70, 60]

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
    turtle.goto(x, y - radius)  # Điều chỉnh vị trí bắt đầu vẽ hình tròn
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()

def draw_tree(turtle, x, y):
    # Vẽ thân cây
    draw_rectangle(turtle, x, y, tree_trunk_width, tree_trunk_height, tree_trunk_color)

    # Vẽ lá cây
    for i, length in enumerate(tree_leaves_lengths):
        draw_triangle(turtle, x - length // 2 + tree_trunk_width // 2, y + tree_trunk_height + i * 30, length, tree_leaves_color)

# Vẽ thân nhà
draw_rectangle(artist, -250, -100, house_width, house_height, house_color)

# Vẽ mái nhà
draw_triangle(artist, -250 - (roof_length - house_width) // 2, 50, roof_length, roof_color)

# Vẽ cửa ra vào
draw_rectangle(artist, -250 + house_width // 2 - door_width // 2, -100, door_width, door_height, door_color)

# Vẽ cửa sổ trái
draw_rectangle(artist, -250 + 20, -10, window_size, window_size, window_color)

# Vẽ cửa sổ phải
draw_rectangle(artist, -250 + house_width - 50, -10, window_size, window_size, window_color)

# Vẽ mặt trời
draw_circle(artist, 200, 200, sun_radius, sun_color)

# Vẽ cây
tree_positions = [50, 150, 250]
for pos in tree_positions:
    draw_tree(artist, pos, -200)

# Ẩn con rùa và hiển thị cửa sổ
artist.hideturtle()
turtle.done()