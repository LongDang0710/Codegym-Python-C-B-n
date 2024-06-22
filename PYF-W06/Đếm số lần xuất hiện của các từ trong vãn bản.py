def count_word_occurrences(text):
    # Khai báo biến num_words là dictionary để lưu các cặp key-value tương ứng với từ và số lần xuất hiện
    num_words = {}

    # Sử dụng hàm split() để tách các từ trong chuỗi truyền vào và lưu thành một mảng
    text_list = text.split()

    # Lặp qua mảng text_list
    for word in text_list:
        # Chuyển các ký tự hoa thành ký tự thường và loại bỏ các khoảng trắng ở đầu và cuối từ
        word = word.lower().strip()

        # Sử dụng hàm get() để lấy giá trị đếm hiện tại của từ lặp trong num_words, nếu không tìm thấy thì giá trị mặc định là 0
        num_words[word] = num_words.get(word, 0) + 1

    # Trả về dictionary num_words chứa số lần xuất hiện của các từ
    return num_words


# Bước 2: Nhận đầu vào từ người dùng
message = input("Nhập văn bản cần đếm từ: ")

# Bước 3: Gọi hàm đếm từ và truyền message làm tham số
word_count = count_word_occurrences(message)

# In ra kết quả đếm từ
for word, count in word_count.items():
    print(f"Từ '{word}' xuất hiện {count} lần.")