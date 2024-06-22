def count_chars(txt):
    result = 0
    for char in txt:
        result += 1
    return result

# Nhận chuỗi muốn đếm của người dùng
input_str = input('Your string: ')

# Gọi hàm đếm và in ra kết quả cho người dùng
print('Length: ', count_chars(input_str))