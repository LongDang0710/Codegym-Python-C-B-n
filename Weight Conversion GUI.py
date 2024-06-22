import tkinter as tk
from tkinter import StringVar, END

def convert_weight():
    try:
        kg = float(e2_value.get())
        gram = kg * 1000
        pound = kg * 2.20462
        ounce = kg * 35.274

        t1.delete("1.0", END)
        t1.insert(END, gram)

        t2.delete("1.0", END)
        t2.insert(END, pound)

        t3.delete("1.0", END)
        t3.insert(END, ounce)
    except ValueError:
        t1.delete("1.0", END)
        t1.insert(END, "Invalid input")

        t2.delete("1.0", END)
        t2.insert(END, "Invalid input")

        t3.delete("1.0", END)
        t3.insert(END, "Invalid input")

window = tk.Tk()
window.title("Weight Converter")

# Nhãn thông báo nhập kg
e1 = tk.Label(window, text="Enter weight in Kg:")
e1.grid(row=0, column=0)

# Biến lưu giá trị kg cần chuyển đổi
e2_value = StringVar()
e2 = tk.Entry(window, textvariable=e2_value)
e2.grid(row=0, column=1)

# Nút gọi hàm chuyển đổi trọng lượng
b1 = tk.Button(window, text="Convert", command=convert_weight)
b1.grid(row=0, column=2)

# Nhãn Gram, Pounds và Ounce
e3 = tk.Label(window, text="Gram")
e3.grid(row=1, column=0)

e4 = tk.Label(window, text="Pounds")
e4.grid(row=1, column=1)

e5 = tk.Label(window, text="Ounce")
e5.grid(row=1, column=2)

# Trường chứa giá trị sau khi chuyển đổi
t1 = tk.Text(window, height=1, width=20)
t1.grid(row=2, column=0)

t2 = tk.Text(window, height=1, width=20)
t2.grid(row=2, column=1)

t3 = tk.Text(window, height=1, width=20)
t3.grid(row=2, column=2)

# Gọi vòng lặp sự kiện chính
window.mainloop()