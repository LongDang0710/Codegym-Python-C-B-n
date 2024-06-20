# Bước 1: Nhập vào một số nguyên bất kỳ
num = int(input("Nhập vào một số nguyên: "))

# Bước 2 và 3: Kiểm tra và in kết quả sử dụng toán tử điều kiện ba ngôi
result = "số chẵn" if num % 2 == 0 else "số lẻ"

# In kết quả
print(f"Số {num} là {result}.")