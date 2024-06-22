import turtle
import random
from datetime import datetime

# Thiết lập màn hình
screen = turtle.Screen()
screen.title("Rùa chạy đua")
screen.bgcolor("white")

# Thiết lập đường đua
finish_line = 200

# Tạo các đối tượng rùa
colors = ["red", "blue", "green", "yellow"]
turtle_colors_vietnamese = {
    "red": "đỏ",
    "blue": "xanh dương",
    "green": "xanh lá",
    "yellow": "vàng"
}
turtles = []

for i in range(4):
    t = turtle.Turtle()
    t.color(colors[i])
    t.shape("turtle")
    t.penup()
    t.goto(-250, 100 - i * 50)
    turtles.append(t)

# Biến để lưu thời gian bắt đầu
start_time = None

# Biến để kiểm tra cuộc đua đã bắt đầu hay chưa
race_started = False

# Hàm bắt đầu cuộc đua
def start_race():
    global start_time, race_started
    start_time = datetime.now()
    race_started = True
    while race_started:
        for t in turtles:
            t.forward(random.randint(1, 10))
            if t.xcor() >= finish_line:
                race_started = False
                end_time = datetime.now()
                time_taken = end_time - start_time
                turtle.penup()
                turtle.hideturtle()
                turtle.goto(0, 0)
                winning_color = t.color()[0]
                winning_color_vietnamese = turtle_colors_vietnamese[winning_color]
                turtle.write(f"Rùa {winning_color_vietnamese} thắng cuộc! Thời gian: {time_taken.seconds} giây", align="center", font=("Arial", 16, "bold"))
                screen.ontimer(show_reset_instructions, 3000)  # Hiển thị hướng dẫn reset sau 3 giây
                break

# Hàm để kiểm tra khi nhấn phím bắt đầu
def on_keypress():
    if not race_started:
        start_race()

# Hàm đặt lại cuộc đua
def reset_race():
    turtle.clear()
    for i, t in enumerate(turtles):
        t.goto(-250, 100 - i * 50)
    show_start_instructions()

# Hiển thị hướng dẫn bắt đầu cuộc đua
def show_start_instructions():
    turtle.clear()
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(0, 200)
    turtle.write("Nhấn phím cách để bắt đầu cuộc đua!", align="center", font=("Arial", 16, "bold"))

# Hiển thị hướng dẫn đặt lại cuộc đua
def show_reset_instructions():
    turtle.goto(0, -50)
    turtle.write("Nhấn phím Backspace để đặt lại cuộc đua!", align="center", font=("Arial", 16, "bold"))

# Lắng nghe sự kiện nhấn phím
screen.listen()
screen.onkey(on_keypress, "space")
screen.onkey(reset_race, "BackSpace")

# Hiển thị hướng dẫn bắt đầu cuộc đua lần đầu tiên
show_start_instructions()

# Giữ cửa sổ mở
screen.mainloop()