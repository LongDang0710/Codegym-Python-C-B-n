def get_min_number(numbers):
    result = numbers[0]  # Khởi tạo biến result với giá trị phần tử đầu tiên của mảng

    # Dùng for…in để lặp qua các phần tử trong mảng
    for num in numbers:
        if result > num:  # Kiểm tra và cập nhật giá trị nhỏ nhất
            result = num

    return result  # Trả về giá trị nhỏ nhất


# Nhận đầu vào từ người dùng
input_str = input("Enter a list of numbers separated by spaces: ")

try:
    # Chuyển đổi chuỗi đầu vào thành danh sách các số nguyên
    numbers = list(map(int, input_str.split()))

    # Gọi hàm get_min_number để tìm số nhỏ nhất
    min_number = get_min_number(numbers)

    # In ra kết quả
    print("Min number: ", min_number)
except ValueError:
    print("Error: Please enter a valid list of integer numbers separated by spaces.")