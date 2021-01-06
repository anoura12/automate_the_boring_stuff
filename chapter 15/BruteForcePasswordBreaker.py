from pathlib import Path
import PyPDF2
encrypted = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
dictionary = Path('dictionary.txt')
words = dictionary.read_text()
words = words.split("\n")

dictionary_length = len(words)
for x in range(dictionary_length):
    word = words[x]
    result = encrypted.decrypt(word)
    if(result == 1):
        print("Password is " + word)
        break
    word = word.lower()
    result = encrypted.decrypt(word)
    if(result == 1):
        print("Password is " + word)
        break
    
