# Nhập cân nặng và chiều cao từ người dùng
weight = float(input("Nhập cân nặng (kg): "))
height = float(input("Nhập chiều cao (m): "))

# Tính chỉ số BMI
bmi = weight / (height ** 2)

# Xác định tình trạng cơ thể dựa trên chỉ số BMI
if bmi < 16:
    status = "Gầy cấp độ III"
elif 16 <= bmi < 17:
    status = "Gầy cấp độ II"
elif 17 <= bmi < 18.5:
    status = "Gầy cấp độ I"
elif 18.5 <= bmi < 25:
    status = "Bình thường"
elif 25 <= bmi < 30:
    status = "Thừa cân"
elif 30 <= bmi < 35:
    status = "Béo phì cấp độ I"
elif 35 <= bmi < 40:
    status = "Béo phì cấp độ II"
else:
    status = "Béo phì cấp độ III"

# In ra chỉ số BMI và tình trạng cơ thể
print(f"Chỉ số BMI của bạn là: {bmi:.2f}")
print(f"Tình trạng cơ thể: {status}")