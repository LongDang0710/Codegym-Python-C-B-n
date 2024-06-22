def sort_numbers(num1, num2, num3):
    temp = 0

    # Kiểm tra và sắp xếp để num1 là số nhỏ nhất
    if num2 < num1 and num2 < num3:
        temp = num1
        num1 = num2
        num2 = temp
    elif num3 < num1 and num3 < num2:
        temp = num1
        num1 = num3
        num3 = temp

    # Kiểm tra và sắp xếp để num2 là số nhỏ thứ nhì
    if num3 < num2:
        temp = num2
        num2 = num3
        num3 = temp

    return (num1, num2, num3)


# Nhận chuỗi số muốn đếm của người dùng
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

# Gọi hàm sắp xếp và in ra kết quả cho người dùng
a, b, c = sort_numbers(x, y, z)
print("Original numbers: ", x, y, z)
print("Sorted numbers: ", a, b, c)