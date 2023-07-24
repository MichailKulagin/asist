from sklearn.feature_extraction.text import CountVectorizer  # pip install scikit-learn
from sklearn.linear_model import LogisticRegression
import sounddevice as sd  # pip install sounddevice
import vosk  # pip install vosk
import time
import json
import queue
import torch
import words
from skills import *
import voice
import pyttsx3
import pyautogui as pag
import mouse
import keyboard as kb
talk = pyttsx3.init()
q = queue.Queue()

model = vosk.Model('C:\\Users\\Michail\\Desktop\\asist\model_small\\vosk-model-small-ru-0.22')
#model = vosk.Model('model_small')  # голосовую модель vosk нужно поместить в папку с файлами проекта
# https://alphacephei.com/vosk/
# https://alphacephei.com/vosk/models

# device = sd.default.device  # <--- по умолчанию
device = sd.default.device = 5, 4 #python -m sounddevice просмотр
samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])  # получаем частоту микрофона

def speaker(text):
	language = 'ru'
	model_id = 'v3_1_ru'
	sample_rate = 48000
	speaker = 'xenia'# xenia aidar baya
	put_accent = True
	put_yo = True
	device = torch.device('cpu')#cpu
	text=text
	model, example_text = torch.hub.load(repo_or_dir='snakers4/silero-models',
										model='silero_tts',
										language=language,
										speaker=model_id)
	model.to(device)  # gpu or cpu

	audio = model.apply_tts(text=example_text,
							speaker=speaker,
							sample_rate=sample_rate)
						
	print("Все ок")

	audio = model.apply_tts(text=text,
							speaker=speaker,
							sample_rate=sample_rate,
							put_accent= put_accent,
							put_yo=put_yo)

	print(text)
	sd.play(audio, sample_rate)
	time.sleep(len(audio)/sample_rate)
	sd.stop()

def talks(words):
	print(words)

talk.say("Привет, чем я могу помочь вам?")
talk.runAndWait()
#speaker("Привет, чем я могу помочь вам?")
def callback(indata, frames, time, status):
    '''
    Добавляет в очередь семплы из потока.
    вызывается каждый раз при наполнении blocksize
    в sd.RawInputStream'''

    q.put(bytes(indata))


def recognize(data, vectorizer, clf):
    '''
    Анализ распознанной речи
    '''
    if data =='гуглить':

        print("Говарите что загуглить")
        talk.say("Говарите что загуглить")
        talk.runAndWait()
        time.sleep(3)
        with sd.RawInputStream(samplerate=samplerate, blocksize=16000, device=device[0], dtype='int16',
                               channels=1, callback=callback):

            rec = vosk.KaldiRecognizer(model, samplerate)
            while True:
                data = q.get()
                if rec.AcceptWaveform(data):
                    data = json.loads(rec.Result())['text']
                    recognize(data, vectorizer, clf)
                    print(data)
                    vod = data
                    webbrowser.open('https://duckduckgo.com/?q=' + vod, new=2)
                    break

    if data =='ютюб':

        print("Говарите что надо найти в ютубе")
        talk.say("Говарите что надо найти в ютубе")
        talk.runAndWait()
        time.sleep(3)
        with sd.RawInputStream(samplerate=samplerate, blocksize=16000, device=device[0], dtype='int16',
                               channels=1, callback=callback):

            rec = vosk.KaldiRecognizer(model, samplerate)
            while True:
                data = q.get()
                if rec.AcceptWaveform(data):
                    data = json.loads(rec.Result())['text']
                    recognize(data, vectorizer, clf)
                    print(data)
                    vod = data
                    webbrowser.open('https://www.youtube.com/results?search_query=' + vod, new=2)
                    break
    if data =='чат' or data =='чак':

        print("Говарите что надо найти")
        talk.say("Говарите что надо найти")
        talk.runAndWait()
        time.sleep(3)
        with sd.RawInputStream(samplerate=samplerate, blocksize=16000, device=device[0], dtype='int16',
                               channels=1, callback=callback):

            rec = vosk.KaldiRecognizer(model, samplerate)
            while True:
                data = q.get()
                if rec.AcceptWaveform(data):
                    data = json.loads(rec.Result())['text']
                    recognize(data, vectorizer, clf)
                    print(data)
                    vod = data
                    webbrowser.open('https://www.perplexity.ai/' , new=2)
                    time.sleep(3)
                    pyautogui.moveTo(762, 475)
                    mouse.click('left')
                    kb.write(vod)
                    pag.typewrite(['enter'])
                    break
    # проверяем есть ли имя бота в data, если нет, то return
    trg = words.TRIGGERS.intersection(data.split())

    if not trg:
        return

    # удаляем имя бота из текста
    data.replace(list(trg)[0], '')


    # получаем вектор полученного текста
    # сравниваем с вариантами, получая наиболее подходящий ответ
    text_vector = vectorizer.transform([data]).toarray()[0]
    answer = clf.predict([text_vector])[0]

    # получение имени функции из ответа из data_set
    func_name = answer.split()[0]

    # озвучка ответа из модели data_set
    #voice.speaker(answer.replace(func_name, ''))
    print(answer.replace(func_name, ''))
    talk.say(answer.replace(func_name, ''))
    talk.runAndWait()
    # запуск функции из skills
    exec(func_name + '()')


def main():
    '''
    Обучаем матрицу ИИ
    и постоянно слушаем микрофон
    '''
    print("Запуск модели vosk")
    # Обучение матрицы на data_set модели
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(words.data_set.keys()))

    clf = LogisticRegression()
    clf.fit(vectors, list(words.data_set.values()))

    del words.data_set

    # постоянная прослушка микрофона
    with sd.RawInputStream(samplerate=samplerate, blocksize=16000, device=device[0], dtype='int16',
                           channels=1, callback=callback):

        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                data = json.loads(rec.Result())['text']
                recognize(data, vectorizer, clf)
                print(data)
            # else:
            #     print(rec.PartialResult())


if __name__ == '__main__':
    main()
