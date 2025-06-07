class School:
    def __init__(self):
        self.ages = []
        self.heights = []
        self.weights = []

    def add_data(self,student_num, ages, heights, weights):
        self.student_num = student_num
        self.ages = ages
        self.heights = heights
        self.weights = weights

    def avg_age(self):
        return sum(self.ages) / self.student_num

    def avg_height(self):
        return sum(self.heights) / self.student_num

    def avg_weight(self):
        return sum(self.weights) / self.student_num


def read_school():
    n = int(input())
    ages = list(map(int, input().split()))
    heights = list(map(int, input().split()))
    weights = list(map(int, input().split()))
    school = School()
    school.add_data(n, ages, heights, weights)
    return school


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
