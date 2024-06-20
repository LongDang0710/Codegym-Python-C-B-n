# Bước 1: Nhập vào một số bất kỳ
num = int(input("Nhập vào một số trong phạm vi từ 1 đến 7: "))

# Bước 2, 3 và 4: Kiểm tra và in kết quả
if num == 1:
    print("Monday")
elif num == 2:
    print("Tuesday")
elif num == 3:
    print("Wednesday")
elif num == 4:
    print("Thursday")
elif num == 5:
    print("Friday")
elif num == 6:
    print("Saturday")
elif num == 7:
    print("Sunday")
else:
    print("error, out of range")