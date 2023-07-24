import requests
from bs4 import BeautifulSoup as b
import random

'''

w = 0
for i in range(10):
    w += 1
    URL = f'https://anekdoty.ru/pro-programmistov/page/'+ 'w' +"/"

    r = requests.get(URL)

    soup = b(r.text, 'lxml')
    anekdot = soup.find_all('p')
    clern_aanekdot = [c. text for c in anekdot]

    if w == 1:
        clern_aanekdot_vse = list()
        clern_aanekdot_vse = clern_aanekdot_vse + clern_aanekdot


    if w == 2:

        clern_aanekdot_vse = clern_aanekdot_vse + clern_aanekdot


    if w == 3:
        clern_aanekdot_vse = clern_aanekdot_vse + clern_aanekdot


    if w == 4:
        clern_aanekdot_vse = clern_aanekdot_vse + clern_aanekdot


    if w == 5:
        clern_aanekdot_vse = clern_aanekdot_vse + clern_aanekdot



skolko = len(clern_aanekdot_vse)
#print(skolko)

i = random.randint(0, skolko)
#print(i)
print(clern_aanekdot_vse[i])


with open("anekdot.txt", "w", encoding='utf8') as file:
    print(clern_aanekdot_vse, file=file)

f = open("anekdot.txt", "r", encoding='utf8')
clern_aanekdot_vse = f.readline()
#print(type(clern_aanekdot_vse))
print(clern_aanekdot_vse)
anekdot = clern_aanekdot_vse.split('[')
print(anekdot)
len(anekdot)
'''


w = 4
clern_aanekdot_vse = list()
for i in range(5):
    w += 1
    if w ==5:
        URL = f'https://anekdoty.ru/pro-programmistov/page/' + '5' + "/"
    if w ==6:
        URL = f'https://anekdoty.ru/pro-programmistov/page/' + '6' + "/"
    if w ==7:
        URL = f'https://anekdoty.ru/pro-programmistov/page/' + '7' + "/"
    if w ==8:
        URL = f'https://anekdoty.ru/pro-programmistov/page/' + '8' + "/"
    if w ==9:
        URL = f'https://anekdoty.ru/pro-programmistov/page/' + '9' + "/"
    r = requests.get(URL)
    soup = b(r.text, 'lxml')
    anekdot = soup.find_all('p')
    clern_aanekdot = [c.text for c in anekdot]
    print("Было",len(clern_aanekdot_vse))
    clern_aanekdot_vse = clern_aanekdot_vse + clern_aanekdot
    print("Стало",len(clern_aanekdot_vse))
skolko = len(clern_aanekdot_vse)
print(skolko)
i = random.randint(0, skolko)
#voice.speaker(clern_aanekdot_vse[i])
print(clern_aanekdot_vse[i])