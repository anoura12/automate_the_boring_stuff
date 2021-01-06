from pathlib import Path

#opening the madlibs text doc and the out text doc which will be used to write the final madlibs paragraph
p = Path('madlibs.txt')
madlibs = p.read_text()
fout = open("out.txt", "wt")

#converting the string into an array
madlibs = madlibs.split(" ")
print(madlibs)

#grammar is an array which has all the placeholders in madlibs.txt
grammar = ['ADJECTIVE', 'ADJECTIVE', 'NOUN', 'NOUN', 'PLURALNOUN' , 'GAME' ,'PLURALNOUN']
sentence_length = len(madlibs)
user_choice = []
count = 0

#to get the user's input for all the placeholders
for i in range(len(grammar)):
    if(grammar[i] == 'NOUN'):
        choice = input("Enter a " + grammar[i].lower() + " where the word doesn't start with a vowel. ")
        user_choice.append(choice)
        continue

    choice = input("Enter a " + grammar[i].lower() + " ")
    user_choice.append(choice)

#to put the words given by the user into the placeholder
for x in range(sentence_length):
    word = madlibs[x]
    if(word in grammar):
        madlibs[x] = user_choice[count]
        count += 1

#to convert the array into a string and then write the final paragraph into the out.txt        
madlibs = " ".join(madlibs)
fout.write(madlibs)

