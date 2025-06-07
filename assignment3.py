
genres = {'Horror':0, 'Romance':0, 'Comedy':0, 'History':0 , 'Adventure':0 , 'Action':0}

n = int(input())
data = []
for i in range(n):
    raw_data = str(input())
    raw_data = raw_data.split()
    data.append(raw_data)

for genre in genres.keys():
    for i in range(n):
        for j in range(4):
            if genre == data[i][j]:
                genres[genre] += 1

sorted_genres = sorted(
    genres, 
    key= lambda x: (
        -genres[x],
        x
        )
    )              

for i in range(len(sorted_genres)):
    print(f'{sorted_genres[i]} : {genres[sorted_genres[i]]}')
