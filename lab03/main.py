import sys
import csv

def main():
    # count_words()
    translate()

def translate():
    dictionary = input("Enter the dictionary filename or path to it: ")
    book = input("Enter the text filename or path to it: ")
    words: dict = {}
    translation: list = [""]
    with open(dictionary,"r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            words[row["tm"]]=row["eng"]
    with open(book,"r") as file:
        for line in file:
            text = get_words_from_line(line)
            for word in text:
                if word in words:
                    translation.append(words[word])
                else:

                    translation.append(word)
    with open("translation.txt","w") as file:
        for word in translation:
            file.write(word)
            if(word.endswith(".")):
                file.write("\n")
            else:
                file.write(" ")

def count_words():
    book = input("Enter the filename or path to it: ")
    with open(book,"r") as file:
        dictionary = {}
        answord = []
        answordnumber = 0
        for line in file:
            words = get_words_from_line(line)
            for word in words:
                if word in dictionary:
                    dictionary[word]+=1
                else:
                    dictionary[word]=1
        for word in dictionary.keys():
            if dictionary[word]>answordnumber:
                answordnumber = dictionary[word]
                answord.clear()
                answord.append(word)
            elif dictionary[word] == answordnumber:
                answordnumber = dictionary[word]
                answord.append(word)
        print(f"The word(s) {answord} was used {answordnumber} times!")


def get_words_from_line(line):
    symbols = ['(',')','?',':',';',',','.','!','/','"',"'"]
    for ch in symbols:
        line.replace(ch,' ')

    line = line.lower().strip().split()
    return line

if __name__ == "__main__":
    main()
