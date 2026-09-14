import json
from datetime import date
from pathlib import Path


DATA_FILE = Path(__file__).parent / "loans_data.json"


def load_loans():
    """تحميل بيانات الإعارة من ملف JSON."""

    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data.get("loans", [])


def save_loans(loans):
    """حفظ بيانات الإعارة في ملف JSON."""

    data = {
        "loans": loans
    }

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def borrow_book(user_id, book_id):
    """إعارة كتاب لمستخدم."""

    loans = load_loans()

    # التأكد من أن الكتاب غير معار حالياً
    for loan in loans:
        if loan["book_id"] == book_id and loan["status"] == "borrowed":
            return False, "الكتاب معار حالياً."

    new_loan = {
        "loan_id": get_next_loan_id(loans),
        "user_id": user_id,
        "book_id": book_id,
        "borrow_date": str(date.today()),
        "return_date": None,
        "status": "borrowed"
    }

    loans.append(new_loan)
    save_loans(loans)

    return True, "تمت إعارة الكتاب بنجاح."


def return_book(book_id):
    """إرجاع كتاب إلى المكتبة."""

    loans = load_loans()

    for loan in loans:
        if loan["book_id"] == book_id and loan["status"] == "borrowed":

            loan["return_date"] = str(date.today())
            loan["status"] = "returned"

            save_loans(loans)

            return True, "تم إرجاع الكتاب بنجاح."

    return False, "الكتاب غير معار حالياً."


def get_next_loan_id(loans):
    """إنشاء رقم جديد لعملية الإعارة."""

    if not loans:
        return 1

    return max(loan["loan_id"] for loan in loans) + 1


def get_active_loans():
    """إرجاع جميع الكتب المعارة حالياً."""

    loans = load_loans()

    return [
        loan
        for loan in loans
        if loan["status"] == "borrowed"
    ]


def get_user_loans(user_id):
    """إرجاع عمليات الإعارة الخاصة بمستخدم معين."""

    loans = load_loans()

    return [
        loan
        for loan in loans
        if loan["user_id"] == user_id
    ]


def display_loans(loans):
    """عرض عمليات الإعارة بشكل منظم."""

    if not loans:
        print("لا توجد عمليات إعارة.")
        return

    for loan in loans:
        print("-" * 40)
        print(f"رقم الإعارة : {loan['loan_id']}")
        print(f"رقم المستخدم: {loan['user_id']}")
        print(f"رقم الكتاب  : {loan['book_id']}")
        print(f"تاريخ الإعارة: {loan['borrow_date']}")
        print(f"تاريخ الإرجاع: {loan['return_date']}")
        print(f"الحالة      : {loan['status']}")


def main():
    """تشغيل اختبار بسيط لنظام الإعارة."""

    print("=== نظام إدارة الإعارة ===")

    success, message = borrow_book(
        user_id=101,
        book_id=5
    )

    print(message)

    active_loans = get_active_loans()

    print("\nالكتب المعارة حالياً:")
    display_loans(active_loans)


if __name__ == "__main__":
    main()
