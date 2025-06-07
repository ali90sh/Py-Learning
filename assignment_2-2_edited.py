from datetime import datetime

class AgeCalculator:
    def __init__(self, birth_str):
        try:
            # تبدیل رشته به datetime؛ در صورت نامعتبر بودن ValueError پرتاب می‌شود
            self.birth = datetime.strptime(birth_str, '%Y/%m/%d')
        except ValueError:
            self.birth = None

    def get_age(self):
        if self.birth is None:
            return None
        now = datetime.now()
        # کاهش یک سال اگر هنوز تولد امسال نگذشته
        age = now.year - self.birth.year - ((now.month, now.day) < (self.birth.month, self.birth.day))
        return age

def main():
    s = input().strip()
    calc = AgeCalculator(s)
    age = calc.get_age()
    if age is None:
        print("WRONG")
    else:
        print(age)

if __name__ == "__main__":
    main()
