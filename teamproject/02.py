users = {}          # 회원 정보 저장 {id: password}
current_user = None  # 현재 로그인한 사용자 ID
books = []          # 도서 목록 [{"title":..., "rented_by": None or user_id}]

# 1. 회원 관리
def signup():
    user_id = input("회원 ID 입력: ")
    if user_id in users:
        print("이미 존재하는 ID입니다.")
        return
    password = input("비밀번호 입력: ")
    users[user_id] = password
    print("회원가입 성공!")

def login():
    global current_user
    if current_user:
        print(f"이미 {current_user}님이 로그인 중입니다.")
        return
    user_id = input("로그인 ID 입력: ")
    password = input("비밀번호 입력: ")
    if users.get(user_id) == password:
        current_user = user_id
        print(f"{user_id}님 로그인 성공!")
    else:
        print("ID 또는 비밀번호가 틀렸습니다.")

def logout():
    global current_user
    if current_user:
        print(f"{current_user}님 로그아웃 되었습니다.")
        current_user = None
    else:
        print("로그인된 사용자가 없습니다.")

# 2. 도서 관리
def show_books():
    if not books:
        print("등록된 책이 없습니다.")
        return
    print("\n[도서 목록]")
    for i, book in enumerate(books):
        status = "대여 가능" if book["rented_by"] is None else f"대여중({book['rented_by']})"
        print(f"{i}. {book['title']} - {status}")

def add_book():
    title = input("추가할 책 제목 입력: ")
    books.append({"title": title, "rented_by": None})
    print(f"'{title}' 책이 등록되었습니다.")

def delete_book():
    try:
        book_num = int(input("삭제할 책 번호 입력: "))
        if 0 <= book_num < len(books):
            if books[book_num]["rented_by"] is None:
                deleted = books.pop(book_num)
                print(f"'{deleted['title']}' 책이 삭제되었습니다.")
            else:
                print("대여 중인 책은 삭제할 수 없습니다.")
        else:
            print("존재하지 않는 책 번호입니다.")
    except ValueError:
        print("숫자를 입력하세요.")

# 3. 대여 및 반납 관리
def rent_book():
    if current_user is None:
        print("로그인 후 이용하세요.")
        return
    show_books()
    try:
        book_num = int(input("대여할 책 번호 입력: "))
        book = books[book_num]
        if book["rented_by"] is None:
            book["rented_by"] = current_user
            print(f"'{book['title']}' 책을 대여했습니다.")
        else:
            print("이미 대여 중인 책입니다.")
    except (ValueError, IndexError):
        print("올바른 책 번호를 입력하세요.")

def return_book():
    if current_user is None:
        print("로그인 후 이용하세요.")
        return
    rented_books = [(i, b) for i, b in enumerate(books) if b["rented_by"] == current_user]
    if not rented_books:
        print("대여 중인 책이 없습니다.")
        return
    print("내가 대여한 책:")
    for i, book in rented_books:
        print(f"{i}. {book['title']}")
    try:
        book_num = int(input("반납할 책 번호 입력: "))
        if books[book_num]["rented_by"] == current_user:
            books[book_num]["rented_by"] = None
            print(f"'{books[book_num]['title']}' 책을 반납했습니다.")
        else:
            print("본인이 대여한 책만 반납할 수 있습니다.")
    except (ValueError, IndexError):
        print("올바른 책 번호를 입력하세요.")

def extend_book():
    if current_user is None:
        print("로그인 후 이용하세요.")
        return
    print("대여 연장 완료!")

# 4. 검색 및 메뉴, 프로그램 흐름
def search_books():
    keyword = input("검색할 제목 또는 키워드 입력: ").lower()
    found = False
    for i, book in enumerate(books):
        if keyword in book["title"].lower():
            status = "대여 가능" if book["rented_by"] is None else f"대여중({book['rented_by']})"
            print(f"{i}. {book['title']} - {status}")
            found = True
    if not found:
        print("검색된 책이 없습니다.")

def show_rented_books():
    rented = [b for b in books if b["rented_by"] is not None]
    if rented:
        print("\n[대여 중인 도서 목록]")
        for i, b in enumerate(rented):
            print(f"{i}. {b['title']} (대여자: {b['rented_by']})")
    else:
        print("대여 중인 도서가 없습니다.")

def menu():
    print("\n--- 도서관 시스템 메뉴 ---")
    print("1. 회원가입")
    print("2. 로그인")
    print("3. 로그아웃")
    print("4. 도서 목록 보기")
    print("5. 대여 중인 도서 목록 보기")
    print("6. 책 추가하기")
    print("7. 책 삭제하기")
    print("8. 책 대여하기")
    print("9. 책 반납하기")
    print("10. 대여 연장하기")
    print("11. 책 검색하기")
    print("0. 종료")
    return input("메뉴 선택: ")

def main():
    print("=== 도서관 시스템 ===")
    while True:
        choice = menu()
        if choice == "1":
            signup()
        elif choice == "2":
            login()
        elif choice == "3":
            logout()
        elif choice == "4":
            show_books()
        elif choice == "5":
            show_rented_books()
        elif choice == "6":
            add_book()
        elif choice == "7":
            delete_book()
        elif choice == "8":
            rent_book()
        elif choice == "9":
            return_book()
        elif choice == "10":
            extend_book()
        elif choice == "11":
            search_books()
        elif choice == "0":
            print("프로그램 종료")
            break
        else:
            print("올바른 메뉴를 선택하세요.")

if __name__ == "__main__":
    main()
