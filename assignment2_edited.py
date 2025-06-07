# تعریف تیم‌ها و مقداردهی اولیه آمار
teams = ["Iran", "Portugal", "Spain", "Morocco"]
stats = {
    team: {
        "wins": 0,
        "draws": 0,
        "loses": 0,
        "goals_for": 0,
        "goals_against": 0,
        "points": 0
    }
    for team in teams
}

# ترتیب بازی‌ها در ورودی
matches = [
    ("Iran", "Spain"),
    ("Iran", "Portugal"),
    ("Iran", "Morocco"),
    ("Spain", "Portugal"),
    ("Spain", "Morocco"),
    ("Portugal", "Morocco"),
]

# خواندن شش خط ورودی و به‌روزرسانی آمار
for team1, team2 in matches:
    line = input().strip()      # مثال: "2-1"
    g1_str, g2_str = line.split("-")
    g1, g2 = int(g1_str), int(g2_str)

    # بروزرسانی گل‌ها
    stats[team1]["goals_for"]     += g1
    stats[team1]["goals_against"] += g2
    stats[team2]["goals_for"]     += g2
    stats[team2]["goals_against"] += g1

    # تعیین نتیجه و امتیاز
    if g1 > g2:
        stats[team1]["wins"]   += 1
        stats[team1]["points"] += 3
        stats[team2]["loses"]  += 1
    elif g1 < g2:
        stats[team2]["wins"]   += 1
        stats[team2]["points"] += 3
        stats[team1]["loses"]  += 1
    else:
        stats[team1]["draws"]   += 1
        stats[team2]["draws"]   += 1
        stats[team1]["points"]  += 1
        stats[team2]["points"]  += 1

# مرتب‌سازی تیم‌ها بر اساس:
# 1) امتیاز نزولی
# 2) تعداد برد نزولی
# 3) نام تیم صعودی (حروف الفبا)
sorted_teams = sorted(
    teams,
    key=lambda t: (
        -stats[t]["points"],
        -stats[t]["wins"],
        t
    )
)

# چاپ نهایی
for t in sorted_teams:
    gd = stats[t]["goals_for"] - stats[t]["goals_against"]
    print(f"{t}  wins:{stats[t]['wins']} , "
          f"loses:{stats[t]['loses']} , "
          f"draws:{stats[t]['draws']} , "
          f"goal difference:{gd} , "
          f"points:{stats[t]['points']}")
