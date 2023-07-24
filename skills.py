import os
import webbrowser
import sys
import pyautogui
import mouse
import time
import subprocess
from random import *
import voice
import pyttsx3
talk = pyttsx3.init()
import requests
from bs4 import BeautifulSoup as b
import random



def igra():
    pyautogui.press('w')

def youtube():
    webbrowser.open('https://www.youtube.com', new=2)



def browser():
    '''Открывает браузер заданнный по уполчанию в системе с url указанным здесь'''

    webbrowser.open('https://www.google.com/search?q=', new=2)


def game():
    '''Нужно разместить путь к exe файлу любого вашего приложения'''
    try:
        webbrowser.open('https://vseigru.net/', new=2)
    except:
        voice.speaker('Путь к файлу не найден, проверьте, правильный ли он')



def game_gonki():
    '''Нужно разместить путь к exe файлу любого вашего приложения'''
    try:
        webbrowser.open('https://vseigru.net/igry-mashiny.html', new=2)
    except:
        voice.speaker('Путь к файлу не найден, проверьте, правильный ли он')




def offpc():
    # Эта команда отключает ПК под управлением Windows
    os.system('shutdown /p /f')
    #os.system('shutdown \s')
    print('пк был бы выключен, но команде # в коде мешает;)))')


def weather():
    #print("эта функция ещё не работает")
    '''Для работы этого кода нужно зарегистрироваться на сайте
    https://openweathermap.org или переделать на ваше усмотрение под что-то другое'''
    try:
        params = {'q': 'Rybinsk', 'units': 'metric', 'lang': 'ru', 'appid': '74785636a6488cad1d765891f721a28a'}
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
        if not response:
            raise
        w = response.json()
        voice.speaker(f"На улице {w['weather'][0]['description']} {round(w['main']['temp'])} градусов")

    except:
        voice.speaker('Произошла ошибка при попытке запроса к ресурсу API, проверь код')


def offBot():
    '''Отключает бота'''
    sys.exit()


def passive():
    '''Функция заглушка при простом диалоге с ботом'''
    pass

def vk():
    url = 'https://vk.com/al_im.php'
    webbrowser.open(url)

def robloks():
    os.system("C:/Users/Michail/AppData/Local/Roblox/Versions/version-40b6a27c6c4d46ef/RobloxPlayerLauncher.exe")


def tg():
    os.system('"C:/Users/Michail/AppData/Roaming/Telegram Desktop/Telegram.exe"')

def music():

    webbrowser.open('https://vk.com/audios510989196', new=2)
    time.sleep(2)
    pyautogui.moveTo(612, 161)
    time.sleep(7)
    mouse.click('left')


def shytka():
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
    voice.speaker(clern_aanekdot_vse[i])

def smotrsmehariki():
    w = randint(1, 3)
    if w == 1:
        webbrowser.open('https://www.youtube.com/watch?v=_bL0s9JRVRk', new=2)
    if w == 2:
        webbrowser.open('https://www.youtube.com/watch?v=YDeYrl7bArQ', new=2)
    else:
        webbrowser.open('https://www.youtube.com/watch?v=gthqO4a_jCQ', new=2)

def film():
    #https://www.kinopoisk.ru/
    webbrowser.open('https://www.kinopoisk.ru/', new=2)

def kalkulator ():
    #https://calculator888.ru/kalkulyator-prostoy
    webbrowser.open('https://calculator888.ru/kalkulyator-prostoy', new=2)

def s():
    #C:\Python3.10\Scripts\dist
    #os.system('"C:/Users/Michail/AppData/Roaming/Telegram Desktop/Telegram.exe"')
    os.system('"C:/Python3.10/Scripts/dist/matematik.exe"')

def mani():
    w = randint(1, 2)
    if w == 1:
        talk.say("тебе выпал орел")
        talk.runAndWait()
    if w == 2:
        talk.say("тебе выпала решка")
        talk.runAndWait()
