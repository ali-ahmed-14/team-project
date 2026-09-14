from members.member1.books import (
    add_book,
    show_books,
    search_book,
    delete_book
)

from members.member2.users import (
    add_user,
    show_users,
    search_user,
    delete_user
)

from members.member3.loans import (
    borrow_book,
    return_book,
    show_borrowed_books
)


def show_menu():
    """عرض القائمة الرئيسية."""
    print("\n" + "=" * 40)
    print("       قائمة عرض المهام ")
    print("=" * 40)

    print("1. إدارة الكتب")
    print("2. إدارة المستخدمين")
    print("3. إدارة الإعارة")
    print("0. خروج")

    print("=" * 40)


def books_menu():
    """قائمة إدارة الكتب."""

    while True:
        print("\n--- إدارة الكتب ---")

        print("1. إضافة كتاب")
        print("2. عرض الكتب")
        print("3. البحث عن كتاب")
        print("4. حذف كتاب")
        print("0. رجوع")

        choice = input("اختر العملية: ").strip()

        if choice == "1":
            title = input("أدخل اسم الكتاب: ").strip()
            author = input("أدخل اسم المؤلف: ").strip()

            add_book(title, author)

        elif choice == "2":
            show_books()

        elif choice == "3":
            keyword = input("أدخل اسم الكتاب للبحث: ").strip()

            search_book(keyword)

        elif choice == "4":
            book_id = input("أدخل رقم الكتاب: ").strip()

            delete_book(book_id)

        elif choice == "0":
            break

        else:
            print("❌ اختيار غير صحيح.")


def users_menu():
    """قائمة إدارة المستخدمين."""

    while True:
        print("\n--- إدارة المستخدمين ---")

        print("1. إضافة مستخدم")
        print("2. عرض المستخدمين")
        print("3. البحث عن مستخدم")
        print("4. حذف مستخدم")
        print("0. رجوع")

        choice = input("اختر العملية: ").strip()

        if choice == "1":
            name = input("أدخل اسم المستخدم: ").strip()

            add_user(name)

        elif choice == "2":
            show_users()

        elif choice == "3":
            keyword = input("أدخل اسم المستخدم للبحث: ").strip()

            search_user(keyword)

        elif choice == "4":
            user_id = input("أدخل رقم المستخدم: ").strip()

            delete_user(user_id)

        elif choice == "0":
            break

        else:
            print("❌ اختيار غير صحيح.")


def loans_menu():
    """قائمة إدارة الإعارة."""

    while True:
        print("\n--- إدارة الإعارة ---")

        print("1. إعارة كتاب")
        print("2. إرجاع كتاب")
        print("3. عرض الكتب المستعارة")
        print("0. رجوع")

        choice = input("اختر العملية: ").strip()

        if choice == "1":
            user_id = input("أدخل رقم المستخدم: ").strip()
            book_id = input("أدخل رقم الكتاب: ").strip()

            borrow_book(user_id, book_id)

        elif choice == "2":
            book_id = input("أدخل رقم الكتاب: ").strip()

            return_book(book_id)

        elif choice == "3":
            show_borrowed_books()

        elif choice == "0":
            break

        else:
            print("❌ اختيار غير صحيح.")


def main():
        choice = input("اختر العملية: ").strip()


        elif choice == "2":
            users_menu()
        elif choice == "3":
            loans_menu()

        elif choice == "0":
            break

        else:
            print("❌ اختيار غير صحيح.")


if __name__ == "__main__":
    main()            print("\n👋 شكراً لاستخدام نظام المكتبة.")

            books_menu()
        if choice == "1":

