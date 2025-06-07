
def main():
    
    n = int(input())
    words = {}
    languages = ['English', 'French', 'Dutch']
    for i in range(n):
    
        line = input().strip()
        parts = line.split()
        word = parts[0]
        eng_translation = parts[1]
        french_translation = parts[2]
        dutch_translation = parts[3]

        words[word] = {'English' : eng_translation, 
                       'French' : french_translation, 
                       'Dutch' : dutch_translation}
        
    sentence = input().strip().split()
    translation = sentence
    # for key in words.keys():
    #     print(key)
    # print(words['man']['French'])
    for i, word in enumerate(sentence):
        for key,value in words.items():
            # print(value.values())
            if word in value.values():
                # print('yes')
                translation[i] = key
    
    translation = " ".join(translation)
    print(translation)    
    
if __name__ == '__main__':
    main()