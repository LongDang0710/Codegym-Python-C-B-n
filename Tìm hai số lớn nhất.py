def find_two_largest_numbers(numbers):
    # Kiểm tra nếu danh sách có ít hơn 2 phần tử
    if len(numbers) < 2:
        raise ValueError("Danh sách phải có ít nhất 2 phần tử")

    # Khởi tạo hai biến để lưu hai số lớn nhất
    largest = second_largest = float('-inf')

    for number in numbers:
        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest and number != largest:
            second_largest = number

    return largest, second_largest


# Hàm để nhận đầu vào từ người dùng
def get_user_input():
    while True:
        user_input = input("Nhập các số, cách nhau bởi dấu cách: ")
        try:
            numbers = list(map(int, user_input.split()))
            if len(numbers) < 2:
                print("Danh sách phải có ít nhất 2 phần tử. Vui lòng thử lại.")
                continue
            return numbers
        except ValueError:
            print("Đầu vào phải là các số nguyên, cách nhau bởi dấu cách. Vui lòng thử lại.")


# Chương trình chính
if __name__ == "__main__":
    while True:
        numbers = get_user_input()
        try:
            largest, second_largest = find_two_largest_numbers(numbers)
            print(f"Hai số lớn nhất là: {largest} và {second_largest}")
            break  # Thoát vòng lặp khi tìm thành công hai số lớn nhất
        except ValueError as e:
            print(f"Lỗi: {e}. Vui lòng thử lại.")