# Bước 1: Cho người dùng nhập biến
input_range = input("Nhập khoảng số (bắt đầu và kết thúc) cách nhau bằng khoảng trắng: ")
start, end = map(int, input_range.split())

# Bước 2: Kiểm tra biến nhập
if end < start:
    print("Số kết thúc cần lớn hơn số bắt đầu")
else:
    # Bước 3: Bắt đầu xử lý việc in kết quả
    for num in range(start, end + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)