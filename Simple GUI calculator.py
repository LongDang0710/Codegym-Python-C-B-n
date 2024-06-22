import tkinter as tk
from tkinter import StringVar, END

# Bước 2: Khởi tạo biến expression
expression = ""

# Bước 3: Khởi tạo hàm cập nhật biểu thức
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Bước 4: Khởi tạo hàm tính biểu thức cuối cùng
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""

# Bước 5: Khởi tạo hàm xoá biểu thức
def clear():
    global expression
    expression = ""
    equation.set("")

# Bước 6: Khởi tạo cửa sổ GUI
window = tk.Tk()
window.configure(background="light green")
window.title("Simple Calculator")
window.geometry("275x250")

# Bước 7: Cài đặt cửa sổ GUI
equation = StringVar()
expression_field = tk.Entry(window, textvariable=equation)
expression_field.grid(columnspan=4, ipadx=70)

# Bước 8: Khởi tạo các nút bấm số và toán tử
buttons = [
    '1', '2', '3', '+',
    '4', '5', '6', '-',
    '7', '8', '9', '*',
    '0', '.', 'Clear', '/',
    '='
]

row = 1
col = 0

for button in buttons:
    if button == '=':
        tk.Button(window, text=button, fg='black', bg='red',
                  command=equalpress, height=2, width=7).grid(row=row, column=col)
    elif button == 'Clear':
        tk.Button(window, text=button, fg='black', bg='red',
                  command=clear, height=2, width=7).grid(row=row, column=col)
    else:
        tk.Button(window, text=button, fg='black', bg='white',
                  command=lambda b=button: press(b), height=2, width=7).grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

# Bước 9: Gọi vòng lặp sự kiện chính
window.mainloop()