'''
Using names.txt, a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name,
 multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
 is the 938th name in the list. So, COLIN would obtain a score of 938 * 53 = 49714.
 
What is the total of all the name scores in the file?
'''
import re


def getalphascore(name):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    namescore = 0
    for posi in range(len(name)):
        letter = name[posi]
        namescore += (alphabet.index(letter)+1)
    return namescore

def calcallnames(listofnames):
    totalnamescore= 0
    for name in listofnames:
        totalnamescore += (getalphascore(name)*(listofnames.index(name)+1))
    return totalnamescore



with open('names.txt', mode='r') as file:
    text = file.read()

text = re.sub('"', '', text)

names = re.split(',', text)

'''
print(names)
names.sort()
print(names)
print(names.index("COLIN")+1)
print(getalphascore("COLIN")*(names.index("COLIN")+1))
'''
print(calcallnames(names))
