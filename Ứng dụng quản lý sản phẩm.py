def get_product_info(products, product_id):
    """Hàm lấy thông tin sản phẩm bằng id sản phẩm"""
    if product_id in products:
        return products[product_id]
    return None


def update_product(products, product_id, product_name):
    """Hàm cập nhật danh sách sản phẩm"""
    products[product_id] = product_name


def display_products(products):
    """Hàm hiển thị danh sách sản phẩm"""
    if not products:
        print("Danh sách sản phẩm trống.")
    else:
        print("Danh sách sản phẩm hiện tại:")
        for product_id, product_name in products.items():
            print(f"ID: {product_id}, Tên: {product_name}")


def main():
    products = {}  # Khởi tạo danh sách sản phẩm
    while True:
        # Bước 5: In ra màn hình các lựa chọn mà người dùng có thể chọn để thực hiện
        print("\nChọn một tùy chọn quản lý sản phẩm:")
        print("1. Thêm sản phẩm mới")
        print("2. Cập nhật sản phẩm")
        print("3. Xóa sản phẩm")
        print("4. Hiển thị danh sách sản phẩm")
        print("5. Thoát")

        # Bước 6: Khai báo biến option, mang giá trị phương thức quản lý mà người dùng muốn thực hiện
        option = int(input("Nhập lựa chọn của bạn: "))

        # Bước 7: Dùng if…elif…else để kiểm tra giá trị của biến option và thực hiện các hàm theo đúng giá trị đó
        if option == 1:  # Thêm sản phẩm mới
            product_id = int(input("Nhập ID sản phẩm: "))
            if get_product_info(products, product_id):
                print("Sản phẩm với ID này đã tồn tại.")
            else:
                product_name = input("Nhập tên sản phẩm: ")
                update_product(products, product_id, product_name)
                print("Thêm sản phẩm thành công.")

        elif option == 2:  # Cập nhật sản phẩm
            product_id = int(input("Nhập ID sản phẩm cần cập nhật: "))
            if get_product_info(products, product_id):
                product_name = input("Nhập tên sản phẩm mới: ")
                update_product(products, product_id, product_name)
                print("Cập nhật sản phẩm thành công.")
            else:
                print("Sản phẩm với ID này không tồn tại.")

        elif option == 3:  # Xóa sản phẩm
            product_id = int(input("Nhập ID sản phẩm cần xóa: "))
            if get_product_info(products, product_id):
                del products[product_id]
                print("Xóa sản phẩm thành công.")
            else:
                print("Sản phẩm với ID này không tồn tại.")

        elif option == 4:  # Hiển thị danh sách sản phẩm
            display_products(products)

        elif option == 5:  # Thoát khỏi ứng dụng
            print("Thoát khỏi chương trình.")
            break

        else:  # Lựa chọn không hợp lệ
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")

        # Bước 8: In ra danh sách sản phẩm sau khi quản lý
        display_products(products)


if __name__ == "__main__":
    main()