"""
FUNGUJÍCÍ VERZE NA opravit.py

1. slova z textu do seznamupo jednom slově  MÁM
2. řešení zvláštních znaků  1.ČÁST MÁM
    (jednotlivá slova jako elementy v seznamu--> sčekuje jestli první nebo poslední znak elementu je v seznamu zvláštních znaků, když je, vymaže znak a přidá do library společně s místem ze kterého to vzalo ( rizikové jednoznakové elementy))
3. sčekování jednotlivých slov jestli jsou v seznamu, případně nalezení nejpodobnějších, z podobných pak vybere nejčastější slova
4. opětovné bepsání do textu

PROBLÉMY:
- nezvládne vyřešit chybějící mezeru, čili spojená dvě slova
"""
import json
import sys
from difflib import get_close_matches


dictionary_path = 'syn2015_word_abc_utf8.tsv'


text = []
textodst = []
otext = "" #opravený text
p = 0

pocet_radku = 0

slovnik = {}

if len(sys.argv) == 2:
    _, input_path = sys.argv  # poté, co to bude aspoň trochu fungovat přidat output file


with open(input_path, 'r',encoding="utf8") as input_file: # přepsání textu do listu
    f = input_file.read()
    #print(len(f.split("\n")))
    """for line in f: #kolik řádků
        line = line.strip("")
        pocet_radku += 1
    print(pocet_radku)"""
    for odst in f.split("\n"):
        t= [odst]
        text.append(odst)

    print(text)
    """for odstavec in text:
        print(odstavec)

        try:
            if odstavec[0].count(" ") != len(odstavec[0]): # aby nedošlo k chybě že split nemá co splitovat
                text.append(odstavec[0].split(" "))
            else:
                text.append(odstavec[0])
            p+=1
        except IndexError:
            #print(odstavec, odstavec[0])
            print("a už to nefachá  " + str(p))"""


print(text)

"""   NEFUNGUJE- Mělo by to souboru se slovy na konci  řádků vkládat specifickou sadu znaků (např.@#$#)    kterou pak při čtení najdu a na daném místě udělám další řádek
    for line in f:
        line = line.strip("\n")
        pocet_radku += 1
    print(pocet_radku)
    input_file.seek(0,0)
    for x in range(0,pocet_radku):
        f = input_file.readline()
        print(f)
        for line in f.split(" "):
            text.append(line)
        #text.append("@#$%")
        #for word in line.split(" "):

        #text.append("$#@!") #označuje konec řádku
"""


def najdi_zvlastni_znaky(txt): #najde zvláštní znaky vyndá je ze seznamu a přířadí k nim číslo místa, kde se nacházeli (v textu, ve slově(poslední první jinak bby mohl nastat problém s změnou indexu po smazání či přidání písmen))
    zvlastni_znaky_text = []
    zvlastni_znaky = "°1234567890%/('!:_?;+=´)¨§,.-\|€Łł}#[]{@&" + '"'
    mslova = 0
    modstavce = 0
    #global text

    for odst in txt:
        for word in odst:
            mpismene = 0
            for pismeno in word:
                znak = zvlastni_znaky.find(pismeno)
                if znak > 0:
                    zvlastni_znaky_text.append((pismeno, mpismene, mslova, modstavce))

                mpismene += 1
            mslova += 1
        modstavce += 1

    for poradi in zvlastni_znaky_text: #vyhodi zvlastni znaky
        if poradi[0] in text[poradi[2]]:
            # kdyby bylo více stejných zvláštních znaků v jednom slově
            text[poradi[2]] = text[poradi[2]].replace(poradi[0], "")

    return zvlastni_znaky_text


def load_vocabulary(path):
    with open(path, 'r', encoding="utf8") as input_file:
        for line in input_file:

            fields = line.split('\t')
            # word = fields[1]
            rank, word, frq = fields

            frq = int(frq)
            slovnik[word] = frq


def cekuj():
    global otext
    p = 0
    po = 0

    #podobne =  []
    for odst in text:
        for slovo in odst:
            if slovo in slovnik:
                 None
            elif len(get_close_matches(slovo, slovnik)) > 0:
                lp = 0
                lpp = 0
                lhfrq = 0

                podobne = get_close_matches(slovo, slovnik.keys(), 3, 0.4)# zrychlit a upřesnit

                for slovicko in podobne:
                    if slovnik[slovicko] > lhfrq + 700:
                        lpp = lp
                    lp += 1



                text[po][p] = text[po][p].replace(text[po][p], podobne[lpp])

            print(p)
            p += 1
        po += 1





def zvlast_vracec():
    global text
    for znak_poloha in zvlastni_znaky: #pismeno, mpismene, mslova, modstavce
        pol_del_slov = len(text[znak_poloha[2]]) / 2
        if pol_del_slov > znak_poloha[1]:
            text[znak_poloha[3]][znak_poloha[2]] = znak_poloha[0] + text[znak_poloha[3]][znak_poloha[2]]

        else:
            text[znak_poloha[3]][znak_poloha[2]] = text[znak_poloha[3]][znak_poloha[2]] + znak_poloha[0]



def prepis (): # vytvoří dokument do kterého vepíše opravený text
    global otext



    with open("oprav_volanskydum.txt", "w", encoding="utf8") as dokument:
        for odst in text:
            for slovo in odst:
                otext += " " + slovo
            dokument.write(otext)
            dokument.write("\n")



zvlastni_znaky = najdi_zvlastni_znaky(text)

load_vocabulary(dictionary_path)
cekuj()
zvlast_vracec()
prepis()

"""
print(input_file)


#print(textodst)


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