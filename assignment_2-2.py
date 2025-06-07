from datetime import datetime
class Age(datetime):
    
    def age_calculator(self):
        now = datetime.now() 
        if self.year > now.year or self.year < 0 or self.month > 12 or self.day > 31:
            print('WRONG')

        else:
            bd = datetime(self.year, self.month, self.day)
            if now.month < self.month:
                print(now.year - bd.year)
            elif now.month == self.month:
                if now.day < self.day:
                    print(now.year - bd.year)
                else:
                    print(now.year - bd.year + 1)
            else:
                print(now.year - bd.year + 1) 


birthday = input().strip()
year = int((birthday.split('/'))[0])
month = int((birthday.split('/'))[1])
day = int((birthday.split('/'))[2])
age = Age(year, month, day)
age.age_calculator()