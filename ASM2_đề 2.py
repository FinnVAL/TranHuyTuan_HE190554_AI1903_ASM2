class Books:
    def __init__(self, Ten_sach, Ten_tac_gia, Nha_xuat_ban, Nam_XB, Gia_ban):
        self.Ten_sach = Ten_sach
        self.Ten_tac_gia = Ten_tac_gia
        self.Nha_xuat_ban = Nha_xuat_ban
        self.Nam_XB = Nam_XB
        self.Gia_ban = Gia_ban

class BookManagementSystem:
    def __init__(self):
        self.books = []

    def display_main_menu(self):
        print("Main Menu:")
        print("1. Nhap thong tin cua n cuon sach cua FU")
        print("2. In ra man hinh thong tin vua nhap")
        print("3. Sap xep thong tin giam dan theo nam xuat ban va hien thi")
        print("4. Tim kiem theo ten sach")
        print("5. Tim kiem theo ten tac gia")
        print("6. Thoat")

    def function1(self):
        while True:
            try:
                n = int(input("Bạn muốn nhập vào bao nhiêu cuốn sách? "))
                m = n
                with open('FU.txt','w', encoding="utf-8") as f:
                    f.write(f'{str(m)}')
                    f.close()
                break
            except:
                print("Hãy nhập vào 1 số nguyên dương!")
                continue
        while n != 0:

            while True:
                Ten_sach = input("Nhập vào tên sách: ")
                if len(Ten_sach.strip()) > 30:
                    print("Tên sách không thể chứa quá 30 ký tự!")
                    continue
                if Ten_sach.strip():
                    break
                else:
                    print("Tên sách không thể bị bỏ trống!")
                    continue

            while True:
                Ten_tac_gia = input("Nhập vào tên tác giả: ")
                if len(Ten_tac_gia.strip()) > 30:
                    print("Tên tác giả không thể chứa quá 30 ký tự!")
                    continue
                if Ten_tac_gia.strip():
                    break
                else:
                    print("Tên tác giả không thể bị bỏ trống!")
                    continue

            while True:
                Nha_xuat_ban = input("Nhập vào tên nhà xuất bản: ")
                if len(Nha_xuat_ban.strip()) > 20:
                    print("Tên nhà xuất bản không thể chứa quá 20 ký tự!")
                    continue
                if Nha_xuat_ban.strip():
                    break
                else:
                    print("Tên nhà xuất bản không thể bị bỏ trống!")
                    continue

            while True:
                try:
                    Nam_XB = int(input("Nhập vào năm xuất bản: "))
                    break
                except:
                    print("Hãy nhập vào 1 số nguyên!")
                    continue

            while True:
                try:
                    Gia_ban = int(input("Nhập vào giá bán: "))
                    break
                except:
                    print("Hãy nhập vào 1 số nguyên")
                    continue
            print('')

            books = Books(Ten_sach, Ten_tac_gia, Nha_xuat_ban, Nam_XB, Gia_ban)
            self.books.append(books)

            with open('FU.txt','a',encoding="utf-8") as f:
                f.write(f'\n{Ten_sach}\n')
                f.write(f'{Ten_tac_gia}\n')
                f.write(f'{Nha_xuat_ban}\n')
                f.write(f'{str(Nam_XB)}\n')
                f.write(f'{str(Gia_ban)}\n')
                f.close()
            n = n - 1
        print("Nhập thông tin", m ,"cuốn sách thành công.")

    def function2(self):
        with open('FU.txt', 'r', encoding='utf-8') as f:
            num_books = int(f.readline())
            print("Tổng số cuốn sách:", num_books)
            print(f"{'Tên sách':<30}{'Tên tác giả':<30}{'Năm XB':<10}{'Giá bán':<10}")
            print("=" * 80)
            for i in range(num_books):
                Ten_sach = f.readline().strip()
                Ten_tac_gia = f.readline().strip()
                Nha_xuat_ban = f.readline().strip()
                Nam_XB = int(f.readline().strip())
                Gia_ban = int(f.readline().strip())
                f.readline()
                print(f"{Ten_sach:<30}{Ten_tac_gia:<30}{Nam_XB:<10}{Gia_ban}")
            print("=" * 80)
            f.close()

    def function3(self):
        self.books = []

        with open('FU2022.txt', 'w', encoding='utf-8') as i:
            with open('FU.txt','r') as k:
                num_books = int(k.readline().strip())
                k.close()
            i.write(f'{num_books}')
            i.close()

        with open('FU.txt', 'r', encoding='utf-8') as f:
            num_books = int(f.readline().strip())
            for _ in range(num_books):
                Ten_sach = f.readline().strip()
                Ten_tac_gia = f.readline().strip()
                Nha_xuat_ban = f.readline().strip()
                Nam_XB = int(f.readline().strip())
                Gia_ban = int(f.readline().strip())
                f.readline()

                book = Books(Ten_sach, Ten_tac_gia, Nha_xuat_ban, Nam_XB, Gia_ban)
                self.books.append(book)
            f.close()

        sorted_books = sorted(self.books, key=lambda x: (x.Nam_XB, x.Gia_ban), reverse=True)

        print(f'Tổng số cuốn sách: {num_books}')
        print(f"{'Tên sách':<30}{'Tên tác giả':<30}{'Năm XB':<10}{'Giá bán':<10}")
        print("=" * 80)
        for book in sorted_books:
            print(f"{book.Ten_sach:<30}{book.Ten_tac_gia:<30}{book.Nam_XB:<10}{book.Gia_ban}")
            with open('FU2022.txt','a',encoding="utf-8") as t:
                t.write(f'\n{book.Ten_sach}\n')
                t.write(f'{book.Ten_tac_gia}\n')
                t.write(f'{book.Nha_xuat_ban}\n')
                t.write(f'{str(book.Nam_XB)}\n')
                t.write(f'{str(book.Gia_ban)}\n')
                t.close()
        print("=" * 80)

    def function4(self):
        self.books = []
        with open('FU.txt', 'r', encoding='utf-8') as f:
            num_books = int(f.readline().strip())
            for _ in range(num_books):
                Ten_sach = f.readline().strip()
                Ten_tac_gia = f.readline().strip()
                Nha_xuat_ban = f.readline().strip()
                Nam_XB = int(f.readline().strip())
                Gia_ban = int(f.readline().strip())
                f.readline()

                book = Books(Ten_sach, Ten_tac_gia, Nha_xuat_ban, Nam_XB, Gia_ban)
                self.books.append(book)

        found = False
        search_term = input("Nhập vào tên sách: ")

        for book in self.books:
            if search_term == book.Ten_sach:
                print(f"{book.Ten_sach}, {book.Ten_tac_gia}, {book.Nha_xuat_ban}")
                found = True

        if not found:
            print("Khong tim thay cuon sach nao!")

    def function5(self):
        self.books = []
        with open('FU.txt', 'r', encoding='utf-8') as f:
            num_books = int(f.readline().strip())
            for _ in range(num_books):
                Ten_sach = f.readline().strip()
                Ten_tac_gia = f.readline().strip()
                Nha_xuat_ban = f.readline().strip()
                Nam_XB = int(f.readline().strip())
                Gia_ban = int(f.readline().strip())
                f.readline()

                book = Books(Ten_sach, Ten_tac_gia, Nha_xuat_ban, Nam_XB, Gia_ban)
                self.books.append(book)
                
        found = False
        search_term = input("Nhập vào tên tác giả: ")
        count = 0

        for book in self.books:
            if search_term == book.Ten_tac_gia:
                count = count + 1
                found = True
                print(f"{book.Ten_tac_gia}, {book.Ten_sach}, {count}")

        if not found:
            print("Khong tim thay tac gia tren!")

    def function6(self):
        print("Đang thoát...")
    
    def run(self):
        while True:
            self.display_main_menu()
            choice = input("Nhập vào lựa chọn của bạn: ")
            if choice == '1':
                self.function1()
            elif choice == '2':
                self.function2()
            elif choice == '3':
                self.function3()
            elif choice == '4':
                self.function4()
            elif choice == '5':
                self.function5()
            elif choice == '6':
                self.function6()
                break
            else:
                print("Đã nhập lỗi, hãy nhập lại!")

BookManagementSystem().run()
