"""
1. slova z textu do seznamupo jednom slově
2. řešení zvláštních znaků
    (jednotlivá slova jako elementy v seznamu--> sčekuje jestli první nebo poslední znak elementu je v seznamu zvláštních znaků, když je, vymaže znak a přidá do library společně s místem ze kterého to vzalo ( rizikové jednoznakové elementy))
3. sčekování jednotlivých slov jestli jsou v seznamu, případně nalezení nejpodobnějších, z podobných pak vybere nejčastější slova
4. opětovné bepsání do textu
"""
import sys
import json
from difflib import get_close_matches

print( len(sys.argv))
dictionary_path = 'syn2015_word_utf8.tsv'
if len(sys.argv) == 2:
    _ ,  input_path = sys.argv #poté, co to bude aspoň trochu fungovat přidat output file



text=[]
textodst= []
p = 0

f = open(input_path, 'r')
print(f.read())
"""with open(input_path, 'r') as input_file:
    print( input_file.read())"""

"""
   for line in f:
        for word in line.split():
           textodst.append(word)"""

"""print(input_file)
    content = "hallo ich, bin Patrik!"
    textodst= content.split(" ")
    for x in range(0,len(textodst)):
        text.append(textodst[x].split())"""

print(textodst)
  

"""
vocabulary = {}

# řešení zvláštních znaků - jednotlivá slova jako elementy v seznamu--> sčekuje jestli první nebo poslední znak elementu je v seznamu zvláštních znaků, když je, vymaže znak a přidá do library společně s místem ze kterého to vzalo ( rizikové jednoznakové elementy)

def correct_text(text):
  words = text.split(' ')
  for word in words:
    if word not in vocabulary: # TODO optimize
      print(word)
    
def     
def load_vocabulary(path):
  with open(path, 'r') as input_file:
    for line in input_file:
      fields = line.split('\t')
      # word = fields[1]
      rank, word, frq, _, _, _, _, _ = fields
              
      vocabulary[rank] = (word,frq)
      
def cekuj(text):
    for slovo in text:
        if slovo in vocabulary:
            otxt += " " + slovo
        else:
            if len(get_close_matches(slovo, vocabulary)) > 0:
                podobne = get_close_matches(slovo, vocabulary.items()[0])
                
                
  
load_vocabulary(dictionary_path_path)
user_text = input('enter text to correct: ')



correct_text(user_text)
# prace se terminalem
# ls - ukaže co je ve společné složce
# cd - posune se do zvolené složky
"""
"""
import json
from difflib import get_close_matches
data = json.load(open("data.json"))
vocabulary = []
for x in data.keys():
    vocabulary.append(x)

i = input("Write and I'll check: ")
text = i.split()
otxt=""
def cekuj(text):
    for slovo in text:
        if slovo in data.keys():
            otxt += " " + slovo
        else:
            if len(get_close_matches(slovo, data.keys())) > 0:
                yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
                if yn == "Y":
                    return
                elif yn == "N":
                    return "Slovo n"
                else:
                    return "We didn't understand your entry."
            else:
                return "The word doesn't exist. Please double check it."

print(text)





correct_text(user_text)

"""