import random


def play_game():
    # Bước 2.1: Khai báo biến tổng số đếm với giá trị khởi tạo = 0
    current_number = 0

    # Bước 2.2: Quyết định ai sẽ là người chơi hiện tại
    current_player = "human" if random.randint(0, 1) == 0 else "computer"

    # Bước 2.3: Vòng lặp đếm số
    while current_number <= 21:
        print(f"Số hiện tại: {current_number}")

        if current_player == "human":
            player_choice = ""
            while player_choice not in ['1', '2', '3']:
                player_choice = input("Nhập vào 1, 2, hoặc 3: ")
            player_choice = int(player_choice)
            current_number += player_choice

            if current_number >= 21:
                print(f"Số hiện tại: {current_number}")
                print("Bạn đã thua!")
                break
            else:
                current_player = "computer"

        else:  # current_player == "computer"
            computer_choice = random.randint(1, 3)
            print(f"Máy chọn: {computer_choice}")
            current_number += computer_choice

            if current_number >= 21:
                print(f"Số hiện tại: {current_number}")
                print("Bạn đã thắng!")
                break
            else:
                current_player = "human"


def main():
    while True:
        play_game()
        play_again = input("Bạn có muốn chơi lại không (y/n)? ").lower()
        if play_again.startswith('y'):
            continue
        else:
            break


if __name__ == "__main__":
    main()