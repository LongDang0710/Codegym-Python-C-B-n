def translate_word(dictionary, word):
    for key in dictionary:
        if key == word:
            return dictionary[key]
    return None


# Danh sách các từ được lưu trữ sẵn trong một Dictionary
dictionary = {
    "hello": "xin chào",
    "goodbye": "tạm biệt",
    "thank you": "cảm ơn",
    "yes": "vâng",
    "no": "không"
}

while True:
    # Bước 2: Khai báo biến input_word, mang giá trị là từ cần dịch mà người dùng nhập vào
    input_word = input("Nhập từ tiếng Anh cần dịch: ")

    # Bước 3: Gọi hàm tìm từ cần dịch
    translated_word = translate_word(dictionary, input_word)

    # Bước 4: In ra kết quả
    if translated_word:
        print(f"Nghĩa của từ '{input_word}' là: {translated_word}")
        break  # Thoát khỏi vòng lặp khi tìm thấy từ
    else:
        print(f"Từ '{input_word}' không có trong từ điển. Vui lòng thử lại.")