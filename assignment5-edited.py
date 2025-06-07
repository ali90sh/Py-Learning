def main():
    # خواندن متن (تمام خط)
    text = input().strip()

    # تفکیک جمله‌ها بر اساس نقطه
    sentences = text.split('.')

    results = []     # لیست ذخیرهٔ خروجی
    word_index = 0   # شماره‌ی کلمات (از 1 شروع می‌شود)

    for sent in sentences:
        sent = sent.strip()
        if not sent:
            continue

        words = sent.split()
        for i, w in enumerate(words):
            # هر کلمه را شماره‌گذاری می‌کنیم
            word_index += 1

            # حذف نقطه یا ویرگول انتهای کلمه
            w_clean = w.rstrip('.,')

            # اگر عدد بود، از بررسیِ شاخص بودن صرف‌نظر کن
            if w_clean.isdigit():
                continue

            # اگر کلمه، ابتدای جمله است، شاخص نیست
            if i == 0:
                continue

            # اگر شروع با حرف بزرگ انگلیسی بود، شاخص است
            if w_clean and w_clean[0].isupper():
                results.append(f"{word_index}:{w_clean}")

    # اگر هیچ کلمه‌ی شاخصی پیدا نشد
    if not results:
        print("None")
    else:
        # چاپ هر خروجی در یک خط
        for line in results:
            print(line)


if __name__ == "__main__":
    main()
