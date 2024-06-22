def celsius_to_fahrenheit(celsius):
    return (celsius * 1.8) + 32


def main():
    # Nhập vào giá trị độ Celsius từ người dùng
    celsius = float(input("Nhập vào giá trị độ Celsius: "))

    # Chuyển đổi sang độ Fahrenheit
    fahrenheit = celsius_to_fahrenheit(celsius)

    # Hiển thị kết quả
    print(f"Giá trị độ Fahrenheit tương ứng: {fahrenheit:.2f}°F")


if __name__ == "__main__":
    main()