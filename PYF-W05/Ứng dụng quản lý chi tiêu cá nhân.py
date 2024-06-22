def add_item(myTempList, item):
    myTempList.append(item)

def find_index_item(myTempList, item_name):
    result = -1
    length = len(myTempList)
    for i in range(length):
        if myTempList[i]['name'] == item_name:
            result = i
    return result

def remove_item(myTempList, item_name):
    index = find_index_item(myTempList, item_name)
    if index > -1:
        del myTempList[index]
    else:
        print(item_name + " not in list")

# Mảng chi tiêu hiện tại
expenses = []

# In mảng chi tiêu hiện tại
print("Your expenses:", expenses)

# In các phương thức mà người dùng có thể chọn
print("What do you want to do? -\n"\
        "1. Add\n" \
        "2. Remove")

# Lấy yêu cầu từ người dùng
option = int(input("Select option 1 or 2: "))
name_input = input("Item name: ")

# Kiểm tra yêu cầu của người dùng và gọi hàm tương ứng
if option == 1:
    cost_input = int(input("Item cost: "))
    date_input = input("Date: ")
    item = {'name': name_input, 'cost': cost_input, 'date': date_input}
    add_item(expenses, item)
    print("Your expenses: ", expenses)
elif option == 2:
    remove_item(expenses, name_input)
    print("Your expenses: ", expenses)
else:
    print("Invalid input")