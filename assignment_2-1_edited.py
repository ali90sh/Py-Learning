import sys

class School:
    def __init__(self, ages, heights, weights):

        self.ages = ages
        self.heights = heights
        self.weights = weights

    def avg_age(self):
        return sum(self.ages) / len(self.ages)

    def avg_height(self):
        return sum(self.heights) / len(self.heights)

    def avg_weight(self):
        return sum(self.weights) / len(self.weights)


def read_list(expected_n, name):
    values = list(map(int, input().split()))

    return values


def read_school():
    try:
        n = int(input())
    except ValueError:
        print("Error: تعداد دانش‌آموزان باید یک عدد صحیح باشد.")
        sys.exit(1)

    ages = read_list(n, 'سن')
    heights = read_list(n, 'قد')
    weights = read_list(n, 'وزن')

    # اکنون داده‌ها مستقیماً به __init__ ارسال می‌شوند
    return School(ages, heights, weights)


def main():
    # خواندن اطلاعات مدرسه‌ی A
    school_A = read_school()
    # خواندن اطلاعات مدرسه‌ی B
    school_B = read_school()

    # محاسبه و چاپ میانگین‌ها به صورت float با یک رقم اعشار
    print(f"{school_A.avg_age():.1f}")
    print(f"{school_A.avg_height():.1f}")
    print(f"{school_A.avg_weight():.1f}")
    print(f"{school_B.avg_age():.1f}")
    print(f"{school_B.avg_height():.1f}")
    print(f"{school_B.avg_weight():.1f}")

    # مقایسه میانگین قد
    if school_A.avg_height() > school_B.avg_height():
        print("A")
    elif school_A.avg_height() < school_B.avg_height():
        print("B")
    else:
        # در صورت برابری قد، مقایسه میانگین وزن
        if school_A.avg_weight() < school_B.avg_weight():
            print("A")
        elif school_A.avg_weight() > school_B.avg_weight():
            print("B")
        else:
            # در صورت برابری قد و وزن
            print("Same")


if __name__ == "__main__":
    main()
