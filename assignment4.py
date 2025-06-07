def main():
    # لیست‌هایی برای ذخیرهٔ اطلاعات خانم‌ها و آقایان
    women = []
    men   = []

    # خواندن تعداد شرکت‌کنندگان
    n = int(input().strip())

    for _ in range(n):
        line = input().strip()       # مثال: "m.hosSein.python"
        parts = line.split(".")
        gender = parts[0].lower()    # 'm' یا 'f'
        raw_name = parts[1]
        lang = parts[2]

        # استانداردسازی نام: اول حرف بزرگ، بقیه کوچک
        name = raw_name.capitalize()

        # تفکیک بر اساس جنسیت
        if gender == "f":
            women.append((name, lang))
        else:
            men.append((name, lang))

    # مرتب‌سازی هر گروه بر اساس نام (حروف الفبا)
    women.sort(key=lambda x: x[0])
    men.sort(key=lambda x: x[0])

    # چاپ خروجی: اول خانم‌ها، بعد آقایان
    for name, lang in women:
        print(f"f {name} {lang}")
    for name, lang in men:
        print(f"m {name} {lang}")

if __name__ == "__main__":
    main()
