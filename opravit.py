""" FUNGUJÍCÍ KÓD
1. slova z textu do seznamupo jednom slově  MÁM
2. řešení zvláštních znaků  1.ČÁST MÁM
    (jednotlivá slova jako elementy v seznamu--> sčekuje jestli první nebo poslední znak elementu je v seznamu zvláštních znaků, když je, vymaže znak a přidá do library společně s místem ze kterého to vzalo ( rizikové jednoznakové elementy))
3. sčekování jednotlivých slov jestli jsou v seznamu, případně nalezení nejpodobnějších, z podobných pak vybere nejčastější slova
4. opětovné bepsání do textu

PROBLÉMY:
- nezvládne vyřešit chybějící mezeru nebo mezeru uprostřed slova
-strašně pomalé
- nebere v potaz vedlejší slova--> strašně pomalé

Možná zlepšení:
- lépe vykalibrovat nastavení getclosematch a přidávání frq

-výraznější zlepšení možné zkoumáním souvislostí více slov
    použití knihovny jamspell ( https://github.com/bakwc/JamSpell#train )
        - nenašel jsem pro ni knihovnu v češtině
        - mohl bych si ji vytvořit ( pomocí machine learning, na stránkách je to docela dobře popsané, na to ale ještě nejsem dost velkej machr)


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

if len(sys.argv) == 4:
    _, input_path, output_path, odbornost  = sys.argv  # poté, co to bude aspoň trochu fungovat přidat output file
else:
    print("napiš: kromě python opravit.py napiš co chceš opravit, kam to chceš nahrát a od 1 do 5 (5 nejodbornější)jak moc odborný text necháváš přeložit.")
    exit()

odbornost = int(odbornost)
if odbornost > 5: odbornost = 5 #volbu čísel nemám na ničem založenou, přišlo mi to ale jako zajímavý prvek
elif odbornost < 1: odbornost = 1 #kdyby bylo zadáno větší či menší číslo aby kód nevyhazoval blbosti
odbornost = 6 - odbornost


with open(input_path, 'r',encoding="utf8") as input_file: # přepsání textu do listu
    f = input_file.read
    dznak = len(f)

    f = f.replace("\n"," @#$ ")
    text = f.split(" ")



def najdi_zvlastni_znaky(txt): #najde zvláštní znaky vyndá je ze seznamu a přířadí k nim číslo místa, kde se nacházeli (v textu, ve slově(poslední první jinak bby mohl nastat problém s změnou indexu po smazání či přidání písmen))
    zvlastni_znaky_text = []
    zvlastni_znaky = "°1234567890%/('!:_?;+=´)¨§,.-\|€Łł}#[]{@&" + '"'
    mslova = 0

    #global text


    for word in text:
        if word != "@#$": #odstavec
            mpismene = 0
            for pismeno in word:
                znak = zvlastni_znaky.find(pismeno)
                if znak > 0:
                    zvlastni_znaky_text.append((pismeno, mpismene, mslova))

                mpismene += 1
            mslova += 1


    for poradi in zvlastni_znaky_text: #vyhodi z textu zvlastni znaky
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
    progres = ""


    #podobne =  []

    for slovo in text:
        if slovo in slovnik:
            None
        elif slovo == "@#$":
             None
        elif len(get_close_matches(slovo, slovnik)) > 0:
            lp = 0
            lpp = 0
            lhfrq = 0

            podobne = get_close_matches(slovo, slovnik.keys(), 3, 0.4)# zrychlit a upřesnit

            for slovicko in podobne:
                if slovnik[slovicko] > lhfrq + odbornost * 125 + 200: # jestli není nějaký z překladů výrazně častější
                    lpp = lp
                lp += 1

            text[p] = text[p].replace(text[p], podobne[lpp])

        progres2 = str(round((p / len(text)) * 100)) + "%" # informuje o kolik toho už stihl opravit
        if progres != progres2:
            print(progres2)
            progres = progres2


        p += 1


def zvlast_vracec():
    global text
    for znak_poloha in zvlastni_znaky: #pismeno, mpismene, mslova, modstavce
        pol_del_slov = len(text[znak_poloha[2]]) / 2
        if pol_del_slov > znak_poloha[1]:
            text[znak_poloha[2]] = znak_poloha[0] + text[znak_poloha[2]]

        else:
            text[znak_poloha[2]] = text[znak_poloha[2]] + znak_poloha[0]



def prepis (): # vytvoří dokument do kterého vepíše opravený text
    global otext



    with open(output_path, "w", encoding="utf8") as dokument:
        for slovo in text:
            if slovo != "@#$":
                dokument.write(" " + slovo)
            else:
                dokument.write("\n")
        print("opravený soubor uložen do " + output_path)



zvlastni_znaky = najdi_zvlastni_znaky(text)

load_vocabulary(dictionary_path)
cekuj()
zvlast_vracec()
prepis()

"""
correct_text(user_text)
# prace se terminalem
# ls - ukaže co je ve společné složce
# cd - posune se do zvolené složky
"""
