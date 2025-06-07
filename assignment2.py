# Group B World Cup Standings
import pandas as pd
import numpy as np

data = np.zeros(shape = (4,6))
table = pd.DataFrame(data)
table.columns = ['Teams', 'wins', 'loses', 'draws', 'goal difference', 'points']
table['Teams'] = ['Iran', 'Spain', 'Portugal', 'Morocco']

# Input scores
results = []
for i in range(6):
    result = str(input())
    results.append(list(map(int, result.split('-'))))
results = np.array(results)

n = len(table['Teams'])

scores = np.empty((n, n))
indices_up = np.triu_indices(n, 1)
indices_down = np.tril_indices(n, -1)
scores[indices_up] = results[:, 0]
scores[indices_down] = results[:, 1]
scores[np.diag_indices_from(scores)] = -1
scores = scores.astype(int)

def points_calculator(scores):
    
    # Win or Draw or Lose
    for i in range(n):
        for j in range(n):
            if j > i:
                table.loc[i, 'goal difference'] += scores[i, j] - scores[j, i]
                table.loc[j, 'goal difference'] += scores[j, i] - scores[i, j]
                if scores[i, j] > scores[j, i]:
                    table.loc[i, 'wins'] += 1
                    table.loc[j, 'loses'] += 1
                    table.loc[i, 'points'] += 3
                elif scores[i, j] < scores[j, i]:
                    table.loc[i, 'loses'] += 1
                    table.loc[j, 'wins'] += 1
                    table.loc[j, 'points'] += 3
                else:
                    table.loc[i, 'draws'] += 1
                    table.loc[j, 'draws'] += 1
                    table.loc[i, 'points'] += 1
                    table.loc[j, 'points'] += 1

points_calculator(scores)
table.sort_values(by=['points', 'wins', 'Teams'], ascending=[False, False, True], inplace=True)
table = table.reset_index(drop=True)
numeric_columns = table.select_dtypes(include=np.number).columns
table[numeric_columns] = table[numeric_columns].astype(int)
# print(table)

for i in range(n):
    print(f'{table["Teams"][i]}  wins:{table["wins"][i]} , loses:{table["loses"][i]} , draws:{table["draws"][i]} , goal difference:{table["goal difference"][i]} , points:{table["points"][i]}')