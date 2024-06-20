# Bước 1: Nhập vào số tiền người dùng đã chi
amount_spent = int(input("Nhập vào số tiền đã chi tại cửa hàng ($): "))

# Bước 2, 3 và 4: Kiểm tra mức giảm giá và tính tổng số tiền phải thanh toán
if amount_spent >= 150:
    discount = 50
elif amount_spent >= 100:
    discount = 25
elif amount_spent >= 75:
    discount = 15
else:
    discount = 0

total_amount = amount_spent - discount

# In ra tổng số tiền phải thanh toán
print(f"Tổng số tiền phải thanh toán sau khi giảm giá là: ${total_amount}")