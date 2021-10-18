import string
with open("words.txt", "r") as file:
    word_dict={}
    for line in file:
        line = line.strip()
        word_list = line.split()
        for word in word_list:
            word = word.lower().strip().strip(string.punctuation)
            if word not in word_dict:
                word_dict[word]
    print(word_dict)
