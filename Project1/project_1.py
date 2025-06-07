import random

class Person:
    def __init__(self, name):
        self.name = name

class Player(Person):
    def get_name_team(self):
        print(f"{self.name} - Team {self.team}")
        
def main():
    # Names list
    names = 'حسین - مازیار - اکبر - نیما -  مهدی - فرهاد - محمد - خشایار - میلاد - مصطفی - امین - سعید - پویا - پوریا - رضا - علی - بهزاد - سهیل - بهروز - شهروز - سامان - محسن'
    names = names.strip().split('-')
    names = list(map(lambda x: x.strip(), names))
    # print(names)

    # Creating player objects
    players = [Player(name) for name in names]
    
    # Shuffling players
    random.shuffle(players)
    team_A = players[:11]
    team_B = players[11:]
    
    # Assigning team to players
    for p in team_A:
        p.team = 'A'
    for p in team_B:
        p.team = 'B'
    
    # Output
    for p in players:
        p.get_name_team()
        

if __name__ == "__main__":
    main()
