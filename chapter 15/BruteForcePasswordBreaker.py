from pathlib import Path
import PyPDF2

#opens the encrypted file and the text doc with the words of the dictionary
encrypted = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
dictionary = Path('dictionary.txt')
words = dictionary.read_text()
words = words.split("\n") #creates an array of the words in the dictionary

dictionary_length = len(words)

#iterates through the entire dictionary.txt
for x in range(dictionary_length):
    word = words[x]
    result = encrypted.decrypt(word)

    #if the word is the password to open encrypted.txt(gives value of 1), prints the password and stops.
    if(result == 1):
        print("Password is " + word)
        break

    word = word.lower() #checks for the lowercase version of the word as well
    result = encrypted.decrypt(word)
    if(result == 1):
        print("Password is " + word)
        break
    
