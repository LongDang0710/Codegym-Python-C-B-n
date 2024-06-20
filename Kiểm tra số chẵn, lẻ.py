# Bước 1: Nhập vào một số bất kỳ
num = float(input("Nhập vào một số bất kỳ: "))

# Bước 2, 3 và 4: Kiểm tra và in kết quả
if num.is_integer():  # Kiểm tra nếu số là số nguyên
    num = int(num)  # Chuyển đổi thành số nguyên để kiểm tra chia hết
    if num % 2 == 0:
        print(f"Số {num} là số chẵn.")
    elif num % 2 == 1:
        print(f"Số {num} là số lẻ.")
    else:
        print(f"Số {num} không phải là số chẵn hay số lẻ.")
else:
    print(f"Số {num} không phải là số tự nhiên.")