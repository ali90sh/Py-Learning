
text = str(input())
words = text.split()
specials = []
for i, word in enumerate(words):
    if word == word.capitalize():
        if words[i - 1].endswith('.'):
            continue
        word.strip()
        word.strip(',')
        word.strip('.')
        specials.append((word, i + 1))
        
        
for word, i in specials:
    print(f'{i}:{word}')