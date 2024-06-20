# Bước 1: Dùng for…in và range(1, 10) để tạo vòng lặp cho bảng cửu chương từ 1 đến 9
for number in range(1, 10):
    print(f"Bảng cửu chương {number}:")

    # Bước 2: Trong mỗi vòng lặp trên, tiếp tục sử dụng for…in và hàm range(1, 10)
    for i in range(1, 10):
        print(f"{number} x {i} = {number * i}")

    # In ra dòng trống để phân cách giữa các bảng cửu chương
    print()