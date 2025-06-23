def main():
    while True:
        print("選択してください：")
        print("1: とよふく")
        print("2: ふたば")
        print("3: メンバー3の名前")
        print("q: 終了")

        choice = input("> ")

        if choice == "1":
            print("がんばります")
        elif choice == "2":
            print("よろしくお願いします")
        elif choice == "3":
            print("メンバー3のコメント")
        elif choice == "q":
            print("プログラムを終了します。")
            break
        else:
            print("無効な入力です。もう一度選択してください。")

if __name__ == "__main__":
    main()
