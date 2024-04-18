import re

def create_file(nazwa, ile):
    plik = open(nazwa, "w", encoding="utf8")
    for i in range(ile):
        plik.write("Ala ma 2 koty.\n")
        plik.write("Kura.znosi . jajka\n")
        plik.write("\n")
    plik.write("Koniec")
    plik.close()
    
def word_counts(file_name):
    res = dict()
    with open(file_name, "r", encoding="utf8") as file:
        for line in file.readlines():
            words = re.split(r'\W+', line)
            words = list(filter(lambda s: s!='', words))
            for word in words:
                if word in res.keys():
                    count = res.get(word)
                    res[word] = count + 1
                else:
                    res[word] = 1
    return res

create_file("plik", 3)
print(word_counts("plik"))
